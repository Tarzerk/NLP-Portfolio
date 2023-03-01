'''
Program 1: Build separate language models for 3 languages as follows.
a. create a function with a filename as argument
b. read in the text and remove newlines
c. tokenize the text
d. use nltk to create a bigrams list
e. use nltk to create a unigrams list
f. use the bigram list to create a bigram dictionary of bigrams and counts, [‘token1 token2’] ->
count
g. use the unigram list to create a unigram dictionary of unigrams and counts, [‘token’] ->
count
h. return the unigram dictionary and bigram dictionary from the function
i. in the main body of code, call the function 3 times for each training file, pickle the 6
dictionaries, and save to files with appropriate names. The reason we are pickling them in
one program and unpickling them in another is that NLTK ngrams is slow and if you put this
all in one program, you may waste a lot of time waiting for ngrams() to finish.
'''
import os
import pathlib
import pickle

import nltk
import sys
from nltk import word_tokenize, ngrams
from collections import Counter

''


def process_data(file_path):
    if not os.path.isfile(file_path):
        print('Invalid file path, please ensure a correct file has been entered and try again')
        quit()
    with open(pathlib.Path.cwd().joinpath(file_path), 'r') as f:
        raw_text = f.read()
    tokens = word_tokenize(raw_text)
    unigrams = ngrams(tokens, 1)
    bigrams = ngrams(tokens, 2)
    unigram_list = []
    bigram_list = []
    for unigram in unigrams:
        unigram_list.append(unigram)
    for bigram in bigrams:
        bigram_list.append(bigram)
    unigram_dict = create_counts(unigram_list)
    bigram_dict = create_counts(bigram_list)
    return unigram_dict, bigram_dict


def create_counts(ngram_list):
    counts = Counter(ngram_list)
    return counts


if __name__ == '__main__':
    english = process_data("LangId.train.English")
    french = process_data("LangId.train.French")
    italian = process_data("LangId.train.Italian")

    # pickle files
    pickle.dump(english[0], open('english_unigrams.pickle', 'wb'))
    pickle.dump(english[1], open('english_bigrams.pickle', 'wb'))
    pickle.dump(french[0], open('french_unigrams.pickle', 'wb'))
    pickle.dump(french[1], open('french_bigrams.pickle', 'wb'))
    pickle.dump(italian[0], open('italian_unigrams.pickle', 'wb'))
    pickle.dump(italian[1], open('italian_bigrams.pickle', 'wb'))

