"""
A program that gets all unigrams and bigrams of there language test files
and pickles them into dictionaries
"""
import os
import pathlib
import pickle
import nltk
from nltk import word_tokenize, ngrams
from collections import Counter


def process_data(file_path):
    if not os.path.isfile(file_path):
        print('Invalid file path, please ensure a correct file has been entered and try again')
        quit()
    with open(pathlib.Path.cwd().joinpath(file_path), 'r') as f:
        raw_text = f.read()
    tokens = word_tokenize(raw_text)
    unigrams = list(ngrams(tokens, 1))  # tokenizes and converts makes list of ngram tuples
    bigrams = list(ngrams(unigrams, 2))
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}  # counts occurrences of tuples and stores in dict
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}
    return unigram_dict, bigram_dict


if __name__ == '__main__':
    english = process_data("data/LangId.train.English")
    french = process_data("data/LangId.train.French")
    italian = process_data("data/LangId.train.Italian")

    # pickle files
    pickle.dump(english[0], open('english_unigrams.pickle', 'wb'))
    pickle.dump(english[1], open('english_bigrams.pickle', 'wb'))
    pickle.dump(french[0], open('french_unigrams.pickle', 'wb'))
    pickle.dump(french[1], open('french_bigrams.pickle', 'wb'))
    pickle.dump(italian[0], open('italian_unigrams.pickle', 'wb'))
    pickle.dump(italian[1], open('italian_bigrams.pickle', 'wb'))
