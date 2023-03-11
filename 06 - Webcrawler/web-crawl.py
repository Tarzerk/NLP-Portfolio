import pathlib
import requests
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
import os
from nltk.corpus import stopwords
import string
import math
from nltk.stem import WordNetLemmatizer
import pickle


def knowledge_base():
    # handpicked terms based on term frequency output
    kb = {
        'smithing': '/Smithing+Stones',
        'melina': '/melina',
        'talisman': '/Talismans',
        'larval': '/larval+tear',
        'cookbook': '/cookbook',
        'rune': '/runes',
        'affinity': '/Affinities',
        'dlc': '/dlc',
        'divine': '/Divine+Towers',
        'arcs': '/Rune+Arc'
    }
    base_url = 'https://eldenring.wiki.fextralife.com/'
    for term in kb:
        page = requests.get(base_url + kb[term])
        term_soup = BeautifulSoup(page.content, 'html.parser')
        fact = sent_tokenize(term_soup.get_text())
        fact = [s.replace('\n', '').replace('\xa0', '') for s in fact]
        kb[term] = fact[3]

    for key, value in kb.items():
        print(f'{key}: {value}\n')
    return kb


def scrape_link(url, file_path):
    current_page = requests.get(url)
    current_file = open(file_path, 'w')
    current_soup = BeautifulSoup(current_page.content, 'html.parser')
    for p in current_soup.select('p'):
        current_file.write(p.get_text() + '\n')


def tokenize_file(file):
    with open(pathlib.Path.cwd().joinpath(file), 'r') as f:
        raw_text = f.read()
    tokens = sent_tokenize(raw_text)
    return tokens


def clean_output_file(tokens, filepath):
    output = open(filepath, 'w')
    punctuation = set(string.punctuation)
    # custom stop words based on output
    stop_list = [
        'image', 'litchfield', 'fenlon', 'march', 'february', 'published', 'martin', 'page', 'chalk', 'stanton',
        'updated']
    # Loop through each sentence and preprocess
    lemmatizer = WordNetLemmatizer()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        words = word_tokenize(tokens[i])
        # Remove stopwords and punctuation
        words = [word for word in words if
                 word.isalpha() and word not in stopwords.words('english') and word not in punctuation
                 and word not in stop_list]
        # lemmatize words
        lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
        # Join the words back into a sentence
        tokens[i] = ' '.join(lemmatized_words)
        # tokens[i] = ' '.join(words)
        output.write(tokens[i] + '\n')

    return ' '.join(tokens)


def create_tf_dict(tokens, tf_dict):
    tokens = word_tokenize(tokens)
    for t in tokens:
        if t in tf_dict:
            tf_dict[t] += 1
        else:
            tf_dict[t] = 1

    # get term frequencies
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}

    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


def create_directories():
    directory = "scraping"
    directory2 = "parsing"
    if not os.path.exists(directory) and not os.path.exists(directory2):
        os.mkdir(directory)
        os.mkdir(directory2)
    return directory, directory2


num_docs = 20


def calculate_idf(tf_dict, vocab):
    idf_dict = {}
    keys_list = list([key for d in tf_dict for key in d.keys()])

    for term in vocab:
        temp = ['x' for voc in keys_list if term in voc]
        idf_dict[term] = math.log((1 + num_docs) / (1 + len(temp)))

    return idf_dict


def create_tfidf(tf, idf, tf_idf):
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]
    return tf_idf


def main():
    URL = 'https://www.pcgamer.com/elden-ring-guide/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    directory, directory2 = create_directories()

    link_counter = 0
    all_tf_dicts = []
    vocab = set()
    for link in soup.find_all('a', attrs={'href': re.compile('^https://www.pcgamer.com/')}):
        current_link = link.get('href')
        if link_counter < 20 and 'elden' in current_link:
            print(current_link)
            # scrape text from each link
            filename = 'file' + str(link_counter + 1) + '.txt'
            filepath1 = os.path.join(directory, filename)
            scrape_link(current_link, filepath1)

            # clean text from each link
            tokens = tokenize_file(filepath1)
            filename = 'parse' + str(link_counter + 1) + '.txt'
            filepath2 = os.path.join(directory2, filename)
            tokens = clean_output_file(tokens, filepath2)

            # calculate tf
            tf_dict = {}
            tf_dict = create_tf_dict(tokens, tf_dict)
            vocab.update(tf_dict.keys())  # add each key to vocab set
            all_tf_dicts.append(tf_dict)

            link_counter += 1

    print('\nlen of vocab: ', len(vocab))
    print('len of all_tf_dicts: ', len(all_tf_dicts))
    idf_dict = calculate_idf(all_tf_dicts, vocab)
    print('len of idf_dict: ', len(idf_dict))
    # print(idf_dict)
    # print('idf for somber:', idf_dict['somber'])
    # print('idf for elden:', idf_dict['elden'])

    tf_idf = {}
    for dict in all_tf_dicts:
        create_tfidf(dict, idf_dict, tf_idf)
    print('len of tf_idf: ', len(tf_idf), '\n')
    sorted_tf_idf = sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)  # highest tf-id

    print('Top 30 terms using the tf-idf dictionary: ')
    for i, key in enumerate(sorted_tf_idf[:30]):
        print(i+1, '\t', key)

    print('\n')
    kb = knowledge_base()
    pickle.dump(kb, open('knowledge_base.pickle', 'wb'))


if __name__ == '__main__':
    main()
