import heapq
import os
import uuid
import csv
import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from google.cloud import dialogflow_v2 as dialogflow
from eldenbot_api_calls import (get_class_comparison, get_boss_info,
                                get_lvl_recommendations, get_weapon_help,
                                get_class_info, get_stats_help,
                                get_item_info, get_build_help)

API_KEY_PATH = 'API PATH HERE'  # replace this line with the path to your own API Key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = API_KEY_PATH
project_id = 'eldenbot-tbwr'
session_id = str(uuid.uuid4())
DATABASE_PATH = 'user_database.csv'
CONVERSATION_LOG = 'conversation_log.txt'


def append_to_log(text, logfile):
    """
        Functions that logs user interactions to the log
    """
    with open(logfile, "a") as f:
        f.write(text)
        if not text.endswith("\n"):
            f.write("\n")


def top_tfidf_words(filename, n_words=3):
    """
        Does TF-IDF and gets the the top three most common words
    """
    with open(filename, 'r') as f:
        text = f.read()
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray().flatten()
    top_indices = heapq.nlargest(n_words, range(len(tfidf_scores)), key=tfidf_scores.__getitem__)
    top_words = [feature_names[i] for i in top_indices]
    top_scores = [tfidf_scores[i] for i in top_indices]
    
    # prints the top words tf-idf scores and their corresponding terms
    print(f"Top {n_words} TF-IDF Words:")
    for i in range(n_words):
        print(f"{i+1}. Word: {top_words[i]}, TF-IDF Score: {top_scores[i]}")
    
    return top_words


def initialize_database(file_path):
    """
    Function that takes a CSV file path as input
    and returns a dictionary containing each user info and their saved information
    """
    db = {}
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            class_name = row['Class']
            level = row['Level']
            if name in db:
                db[name].append([class_name, level])
            else:
                db[name] = [[class_name, level]]
    return db


def extract_name(sentence):
    """
    Uses NLTK to extract a name from a sentence and returns it
    """
    words = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(words)
    # Extract the proper nouns from the tagged words
    proper_nouns = [word for word, pos in pos_tags if pos == 'NNP' or pos == 'NN']
    # Assume the name is the first proper noun in the sentence
    name = proper_nouns[0]
    return name


def get_response_with_intent(project_id, session_id, text, intent_name):
    """
    Use this whenever we need to get a response based on the intent
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code='en-US')
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session,
        query_input=query_input,
        intent_name=intent_name
    )

    return response


def get_response(project_id, session_id, text):
    """
    Gets the API response from dialogflow and returns it
    as a dictionary
    """
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text=text, language_code='en-US')
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)

    response_dict = {
        'query_text': response.query_result.query_text,
        'speech_recognition_confidence': response.query_result.speech_recognition_confidence,
        'action': response.query_result.action,
        'all_required_params_present': response.query_result.all_required_params_present,
        'fulfillment_text': response.query_result.fulfillment_text,
        'fulfillment_messages': response.query_result.fulfillment_messages,
        'output_contexts': response.query_result.output_contexts,
        'intent': response.query_result.intent,
        'intent_detection_confidence': response.query_result.intent_detection_confidence,
        'diagnostic_info': response.query_result.diagnostic_info,
        'sentiment_analysis_result': response.query_result.sentiment_analysis_result,
    }
    return response_dict


def extract_user_info(text):
    """
    Function that takes the successful user creation response
    and stores it in a set
    """
    regex = r"^Awesome, you are (\w+), your level is (\d+) and you play as a (\w+)$"
    match = re.match(regex, text)
    if match:
        person = match.group(1)
        level = int(match.group(2))
        character_class = match.group(3)
        return (person, level, character_class)
    else:
        return None


def add_user_to_database(file_path, username, userlevel, userclass):
    """
    Adds a new user to the CSV
    """
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        file.write('\n')
        writer.writerow([username, userclass, userlevel])


def get_stats_from_csv(username):
    """
    Adds a new user to the CSV
    """
    data = current_database[username]
    print("Level : " + str(data[0][1]))
    print("Class : " + str(data[0][0]))
    return username, data[0][0], data[0][1]


def update_level(newlevel, username):
    """
    Changes the level of the user in the database
    can only be called for users already there
    """
    with open(DATABASE_PATH, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = {row['Name']: [[row['Class'], row['Level']]] for row in reader}

    data[username][0][1] = newlevel

    with open(DATABASE_PATH, 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Class', 'Level']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for name, info in data.items():
            row = {'Name': name, 'Class': info[0][0], 'Level': info[0][1]}
            writer.writerow(row)

    print(f"{username}'s level has been updated to {newlevel} in the CSV file")


def handle_who_is_boss_intent(response_dict):
    """
    Function to create a follow up question if the user doesnt' give use the
    needed information
    """
    if response_dict['fulfillment_text'] != 'Which boss would you like to learn about?':
        boss_name = response_dict['fulfillment_text']
        print('EldenBot: ' + get_boss_info(boss_name))
    else:
        print('EldenBot: ' + response_dict['fulfillment_text'])


def handle_what_is_item_intent(response_dict):
    """
    Function to create a follow up question if the user doesnt' give use the
    needed information
    """
    if response_dict['fulfillment_text'] != 'Which item would you like to learn about?':
        item_name = response_dict['fulfillment_text']
        print('EldenBot: ' + get_item_info(item_name))
    else:
        print('EldenBot: ' + response_dict['fulfillment_text'])


def handle_compare_classes_intent(response_dict):
    """
    Function to create a follow up question if the user doesnt' give use the
    needed information
    """
    if response_dict['fulfillment_text'] != 'Which classes would you like to compare?':
        tokens = response_dict['fulfillment_text'].split()
        class1 = tokens[0]
        class2 = tokens[2]
        print('EldenBot: ' + get_class_comparison(class1, class2))
    else:
        print('EldenBot: ' + response_dict['fulfillment_text'])
        

if os.path.exists(CONVERSATION_LOG):
    # If the file exists, open it in write mode to delete everything in it
    with open(CONVERSATION_LOG, "w") as f:
        pass  # Pass is a placeholder that does nothing

'''
    Here we gather information about the user to check if they are on
    the database and if not we add them to the database so we can 
    keep track of their data
'''
current_database = initialize_database(DATABASE_PATH)

print('EldenBot: Hi I\'m EldenBot! I am ready to assist you with the game of Elden Ring')
print('EldenBot: Before we start, what is your name?')
text = input('You: ')
username = extract_name(text)
userclass = ""
userlevel = ""
if username in current_database:
    print("Welcome back " + username)
    print("Here are your stats: ")
    username, userclass, userlevel = get_stats_from_csv(username)
else:
    regex = r"^Awesome, you are (\w+), your level is (\d+) and you play as a (\w+)$"
    response_dict = get_response(project_id, session_id, text)
    response_text = response_dict['fulfillment_text']
    print('EldenBot: ' + response_text)
    while userlevel == "" and userclass == "":
        text = input('You: ')
        response_dict = get_response(project_id, session_id, text)
        response_text = response_dict['fulfillment_text']
        if re.match(regex, response_text):
            username, userlevel, userclass = extract_user_info(response_text)
            add_user_to_database('user_database.csv', username, userlevel, userclass)
        print('EldenBot: ' + response_text)

'''
    ChatBot Conversation begins here
    the user may ask any questions
'''
print("What can I do for you today?")
while True:
    text = input('You: ')
    if text.upper() == 'STOP':
        print('EldenBot: Goodbye!')
        break
    append_to_log(text, CONVERSATION_LOG)

    response_dict = get_response(project_id, session_id, text)  # The response from the bot is held here
    '''
        Maps functions to intent 
        For example: If the user asks about weapons, we call get_weapon_help() 
        which will create a text response EldenBot can print to the console
    '''
    intent_functions = {
        'Who is boss?': lambda: handle_who_is_boss_intent(response_dict),
        'What is item?': lambda: handle_what_is_item_intent(response_dict),
        'class info': lambda: print('EldenBot: ' + get_class_info(response_dict['fulfillment_text'])),
        'compare classes': lambda: handle_compare_classes_intent(response_dict),
        'build help': lambda: print(
            'EldenBot: Since you are playing as a ' + userclass + ' considering focusing on the following:\n ' +
            get_build_help(userclass)),
        'stat help': lambda: print('EldenBot: ' + get_stats_help(userclass)),
        'Weapon help': lambda: print('EldenBot: ' + get_weapon_help(userclass)),
        'lvl recommendations': lambda: print('EldenBot: ' + get_lvl_recommendations(userlevel)),
        'update level': lambda: update_level(response_dict['fulfillment_text'], username)
    }

    '''
        Based on Dialog flow response we find what the intent of the user is
        and we call the intent function needed. If the intent isn't found
        we reply with a generic response
    '''
    intent_name = response_dict['intent'].display_name
    if intent_name in intent_functions:
        intent_functions[intent_name]()
    else:
        response_text = response_dict['fulfillment_text']
        print('EldenBot: ' + response_text)
print(top_tfidf_words(CONVERSATION_LOG))