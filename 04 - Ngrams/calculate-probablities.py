'''
A program that opens the pickled dictionaries, reads in a test file, and make guesses on which language it's using on each line.
Then, it reads in the solution file and compares it with the guesses file to compute the accuracy.
'''
import math
import pickle
from nltk import word_tokenize
from nltk.util import ngrams

def get_accuracy() -> float:
    correct_preds = 0
    
    # read solutions
    with open('data/LangId.sol', 'r') as f:
        solutions = f.readlines()
    f.close()
    
    # read guesses
    with open('guesses.txt', 'r') as f:
        guesses = f.readlines() 
    f.close()
    
    # compare each guess and solution
    for i, (guess, sol) in enumerate(zip(guesses, solutions)):
        if guess != sol:
            print("Incorrect prediction at line", i, ": ")
            print("Guess:", guess)
            print("Solution:", sol + '\n')
        else:
            correct_preds += 1
    
    return correct_preds/i * 100


def compute_prob(text: str, unigram_dict: dict, bigram_dict: dict, v: int) -> float:
    p_laplace = 1  # use Laplace smoothing to get probabilities
    unigrams_test = list(ngrams(word_tokenize(text), 1))
    bigrams_test = list(ngrams(unigrams_test, 2))
    
    for bigram in bigrams_test:
        b = bigram_dict[bigram] if bigram in bigram_dict else 0
        u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace += math.log((b + 1 / (u + v)))
        
    return p_laplace
    
    
def main():
    english_unigrams = pickle.load(open('english_unigrams.pickle', 'rb'))
    english_bigrams = pickle.load(open('english_bigrams.pickle', 'rb'))
    french_unigrams = pickle.load(open('french_unigrams.pickle', 'rb'))
    french_bigrams = pickle.load(open('french_bigrams.pickle', 'rb'))
    italian_unigrams = pickle.load(open('italian_unigrams.pickle', 'rb'))
    italian_bigrams = pickle.load(open('italian_bigrams.pickle', 'rb'))
    
    # read test file
    with open('data/LangId.test', 'r', encoding='utf8') as f:
        lines = f.readlines()
    f.close()
    
    index = 1
    output = open("guesses.txt", "w")
    v = len(italian_unigrams) + len(english_unigrams) + len(french_unigrams)
    
    # compute guesses for each line in test file
    for text in lines:
        # get probabilities from english, french, and italian
        prob_en = compute_prob(text,english_unigrams,english_bigrams,v)
        prob_fr = compute_prob(text,french_unigrams,french_bigrams,v)
        prob_it = compute_prob(text,italian_unigrams,italian_bigrams,v)
        
        # put probabilities into dict to get the max val & predict language
        probs_dict = {"English": prob_en,"Italian": prob_it, "French": prob_fr}
        lang = max(probs_dict, key=probs_dict.get)
        output.write(str(index) + ' ' + lang + '\n') # write to output file
        index += 1
        
    output.close()
    print("Accuracy: ", get_accuracy(), '%')

    
if __name__ == '__main__':
    main()