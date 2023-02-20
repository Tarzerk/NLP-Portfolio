import os
import pathlib
import random
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def correct_screen():
    print("""

    (👍^U^)👍

    """)

def death_screen():
    print("""
               ...
             .####_  .
           ;#|\_|/__/|
         ;##/ / \/ \  \\
        ;##/__|O||O|__ \\
       ,##|/_ \_/\_/ _\ |        OOO\\
       ###| | (____) | ||       OOOOO\\
       ;##\/\___/\__/\ //      OOOOOOOO
      ,;####`.      \_)/       / OOOOOOO
    ;#########`. ,,,;./       /  / DOOOOOO
  .';#################;,     /  /     DOOOO
 ,######;######;;;;####;,   /  /        DOOO
;`######`'######;;;##### ,H/  /          DOOO
#`#######`;######;;### ;##H  /            DOOO
##`#######`;######## ;####H /              DOO
`#`#######`;###### ;######H/               DOO
 ###`#######`;; ;#########HH                OO
 ####`#######`;########;###H                OO
 `#####`############;'`#;##H                O
  `#####`########;' /  / `#H
   ######`#####;'  /  /   `H
          
                 R.I.P
          
    """)


def gameover_screen():
    print("""

┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

          """)


def process_data(raw_text):
    # tokenized the text to lower-case raw text,
    lowercase_text = [t.lower() for t in raw_text]
    tokens = [t for t in lowercase_text if t.isalpha()]

    unique_tokens = set(tokens)
    print("The lexical diversity is: " + str(round((len(unique_tokens) / len(tokens)) * 100, 2)) + "%")

    # limited the tokens to not stop words and words with length < 5
    tokens = [t for t in tokens if t not in stopwords.words('english') and t in lowercase_text if len(t) > 5]

    # lemmatized the tokens to make set of unique lemmas
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    lemmas_unique = list(set(lemmas))
    print("The number of unique lemmas in text is: ", len(lemmas_unique))

    # pos tagging on the unique lemmas and prints the first 20 tagged
    unique_tags = nltk.pos_tag(lemmas_unique)
    print("\nThe first 20 unique lemmas in text are: ")
    print(unique_tags[:20])

    # create a list of only those lemmas that are nouns
    tags = nltk.pos_tag(lemmas)
    nouns = []
    for t in tags:
        if t[1] == 'NN':
            nouns.append(t[0])

    print('\nThe number of tokens is ' + str(len(tokens)))
    print('The number of nouns is ' + str(len(nouns)) + '\n')
    return tokens, nouns


def get_most_common_nouns(dictionary):
    nouns_counts_sorted = {k: v for k, v in
                           sorted(dictionary.items(), reverse=True, key=lambda v: v[1])}  # sorts dictionary by value
    common_nouns = list(nouns_counts_sorted.keys())
    common_nouns = common_nouns[:50]
    print('The 50 most common words are: ')
    for i in range(50):
        print(str(i + 1) + '.', common_nouns[i], nouns_counts_sorted[common_nouns[i]])
    return common_nouns


def count_nouns(tokens, nouns):
    counts = dict()
    for t in tokens:
        if t in nouns and t in counts:
            counts[t] += 1
        elif t in nouns:
            counts[t] = 1
    return counts


def flip_board(board, word, letter):
    letter_locations = [pos for pos, char in enumerate(word) if char == letter]  # gets indexes of letter locations
    for index in letter_locations:  # swaps # to the guessed letter in the board
        temp = list(board)
        temp[index] = letter
        board = "".join(temp)
    return board


def guess_game(word_bank):
    print('\nLet us play a guessing game!')
    score = 5
    selected_word = random.choice(word_bank)
    current_board = '_' * len(selected_word)
    user_guess = ''
    guessed_letters = []
    while user_guess != '!':
        print(current_board)
        user_guess = input("Enter a letter to guess: ")
        if user_guess == '!':
            break
        if user_guess in selected_word and user_guess not in guessed_letters:
            guessed_letters.append(user_guess)
            print('Right!')
            current_board = flip_board(current_board, selected_word, user_guess)
            score += 1
        else:
            score -= 1
            print('Sorry, no')
        if score < 0:
            print('\nYou lost, better luck next time!!')
            death_screen()
            quit(0)
        if current_board == selected_word:
            correct_screen()
            print('\nYou got it!! The word was ' + selected_word + '\n')
            selected_word = random.choice(word_bank)
            print('Your new board is listed below: ')
            current_board = '_' * len(selected_word)
        print('Your current score is: ' + str(score))
    print("\nGame over, your total score is: " + str(score))
    gameover_screen()


if __name__ == '__main__':
    if not (len(sys.argv) == 2) or not (os.path.isfile(sys.argv[1])):
        print("Error: file path was not provided or it is not a valid filepath")
        quit()
    file_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(file_path), 'r') as f:
        input_text = f.read().split()
    data = process_data(input_text)
    noun_counts = count_nouns(data[0], data[1])
    most_common_nouns = get_most_common_nouns(noun_counts)
    guess_game(most_common_nouns)
