<p align="center">
  <img src="https://mir-s3-cdn-cf.behance.net/project_modules/1400/0a885470672999.5bf66d0789749.png" />
</p>

# Natural Language Processing Portfolio 🗣️
Hello reader, my name is **Erik** and I would like to welcome you to my **Natural Language Processing Portfolio**. In this collection, I have compiled my first projects in the field of natural language processing, where I explore the different techniques and tools used to process, analyze and generate human language data. As a novice in this field, I am excited to share my learning journey and showcase the skills I have acquired so far. Through these projects, I aim to demonstrate my ability to apply various NLP techniques to solve real-world problems and provide insights into the fascinating world of natural language processing. <br>

## Index 👈
Click on the link to navigate to the desired part. <br>
[Part 0: Overview of NLP](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#overview-of-natural-language-processing)<br>
[Part 1: Simple Processing with Python](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-1--simple-text-processing-with-python-) <br>
[Part 2: Word Guess Game](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-2--word-guess-game-)
[Part 3: WordNet and SentiWordNet](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-3-wordnet-and-sentiwordnet-)

## Overview of Natural Language Processing ✈️
When I think of Natural Language Processing the first thing that comes to mind is a human being able to be understood by a computer. 
NLP just like Machine Learning is part of the field in Artificial Intelligence. It combines computational linguistics to process human speech and text.
#### Natural Language Understanding vs. Natural Language Generation
To draw an example imagine you are having a casual conversation with another person.
Natural Language Understanding whenever you are engaging in a conversation and you are able understand what they are saying
In Natural Language Generation you are able to respond to the person to whom you are speaking with.
The combination of NLU and NLG is what constitutes NLP.
#### Comparing different approaches to NLP
**Rule-Based** <br>

Originating in the 60s. The Rule Based approach works by using rules to check if a piece of text is correct. As an example, we have calculators who may only perform an operation according to the Mathematical order of operation rules. This approach works for best for simple or easily defined rules but it isn’t not very useful for human speech since it is too complex. <br>
**Statistical Approach** <br>

In the late 80s statistical based approaches joined the mix in NLP. It relies by using statistics to guess a desired output of a given problem. As an example, if you were sending a text message and you typed in the word ‘in’ there is a likelihood you might want to use the word ‘the’ and therefore it is suggested. The advantage of models like this is that they don’t require super huge datasets to be useful and may be better than other approaches in that regard. <br>
**Deep Learning** <br>

Deep learning is the most trendy approach NLP approach to date. With the rise of vast computer power and tools like ChatGP3 and Dalle-e. Deep learning works by using huge datasets and algorithms with combinations of statistical and rule based approaches to provide an answer. The main concept is that it starts by having a generalized answer and slowly getting more and more specific. The biggest downside to this approach is that it takes huge computing power and lots of data to provide an accurate model. However, whenever it works it can be scarily accurate. 
#### Personal Interest in NLP
Personally, I decided to learn in NLP since I have been fascinated by tools such as ChatGP3, and Dalle. This tools may not be always accurate however, it is fun to see how the dream of being able to talk to computers is being realized .. at least at a first glance. I would love to use NLP to create a chatbot to create safer gaming servers for children.
#### Sources
NLP with Python by Karen Mazidi

## Assignment #1 : Simple Text Processing with Python 🐍
The goal of the following program is to get comfortable with Python. In this assignment, we take a CSV file as input that contains information such as names, IDs, and phone numbers. Using various functions we sanitize the data and print it to the console. 
### Sample Output
```
The number 555-877.4321 isn't in the correct format '123-456-7890', please re-enter the number: 555-877-4321
The number S4454 isn't in the correct format 'XX1234' , please re-enter the id: SE4454
The ID WH1234 is duplicated in the file, please enter a unique ID in 'XX1234' format: WH6732


Employee list:

Employee id: WH1234
	Smitty S Smith
	555-777-1212

Employee id: SE4454
	Witty W Williams
	555-877-4321

Employee id: OF4321
	Luka L Luka
	555-888-3456

Employee id: WH6732
	Jake X Jason
	555-777-2094

Employee id: SA9384
	Krishna K Krishna
	555-888-0093
```
### Strengths and weaknesse of Python Processsing (in my opinion)
Python processsing can be tedious since you are working with a lot of regular expressions to get the data in the format you want it. 
However, once everything is sanitized operations become way easier which helps when you want to do  machine learning with the 
data obtained. 
In conclusion, it isn't the best thing in the world but it has to be done to get to get to funner aspects of machine 
learning.
### What I learned with this assignment
Through this assignment, I learned how to use Python for the first time. I have done similar data processing with Java however in many ways this was easier since I didn't have to write as much. 
### Link to the source code
You can find the link to the source code as well as the CSV data I used by clicking [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/01%20-%20Simple%20Processing%20with%20Python)

## Assignment 2 : Word Guess Game 🤔
The goal of this program is to get familiar with the NLTK library.
This program uses a text file as input to build a list
of the 50 most common words and creates a hangman style guessing game using the list.
### Sample Output
```
The lexical diversity is: 14.78%
The number of unique lemmas in text is:  1613

The first 20 unique lemmas in text are: 
[('system', 'NN'), ('pumping', 'VBG'), ('malfunction', 'NN'), ('ceaseless', 'NN'), ('tamponade', 'VBD'), 
('performing', 'VBG'),('relatively', 'RB'), ('glossopharyngeal', 'JJ'), ('conduct', 'NN'), ('maintaining', 'NN'),
('frequented', 'VBN'), ('isovolumic', 'JJ'), ('sudden', 'JJ'), ('establish', 'VB'), ('dividing', 'VBG'),
('strongly', 'RB'), ('symptom', 'JJ'), ('survive', 'JJ'), ('dissolve', 'NN'), ('framework', 'NN')]

The number of tokens is 5732
The number of nouns is 2350

The 50 most common words are: 
1. cardiac 109
2. pulmonary 58
3. muscle 58
4. ventricular 54
5. coronary 48
6. atrioventricular 42
7. ventricle 40
8. contraction 38
9. pressure 34
10. condition 32
11. increase 30
12. stimulation 28
13. include 27
14. atrium 25
15. calcium 25
16. surface 23
17. impulse 23
18. resting 22
19. posterior 21
20. septum 20
21. semilunar 20
22. conduction 19
23. percent 19
24. artery 19
25. bundle 19
26. interventricular 18
27. contractile 18
28. inferior 17
29. oxygen 17
30. myocardial 17
31. chordae 16
32. depolarization 16
33. anterior 15
34. opening 15
35. cardiovascular 14
36. pericardial 13
37. period 13
38. activity 13
39. membrane 12
40. supply 12
41. myocardium 12
42. pattern 12
43. treatment 12
44. mitral 12
45. system 12
46. contract 11
47. portion 11
48. connective 11
49. trigger 11
50. patient 10

Let us play a guessing game!
__________
Enter a letter to guess: c
Right!
Your current score is: 6
c____c____
Enter a letter to guess: a
Sorry, no
Your current score is: 5
c____c____
Enter a letter to guess: e
Right!
Your current score is: 6
c___ec___e
Enter a letter to guess: n
Right!
Your current score is: 7
c_nnec___e
Enter a letter to guess: o
Right!
Your current score is: 8
connec___e
Enter a letter to guess: t
Right!
Your current score is: 9
connect__e
Enter a letter to guess: i
Right!
Your current score is: 10
connecti_e
Enter a letter to guess: v
Right!

You got it!! The word was connective
Your new board is listed below: 
Your current score is: 11
_________
Enter a letter to guess: !

Game over, your total score is: 11
```
### What I learned with this assignment
I learned how powerful the Natural Language Took Kit (NLTK) library is. It was able to minimize the amount of code since a lot of
the post processing can be done in just a few lines of code. I also saw how some things might seem inconsistent thereofore it is important to clean up
the data a bit. 
### Link to the source code
You can find the link to the source code as well as the sample text I used by clicking [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/02%20-%20Word%20Guess%20Game%20with%20NLTK)

## Assignment 3: Wordnet and SentiWordNet 🔠
In this assignment we explore the various features of WordNet and SentiWord Net in python.
### What is WordNet?
WordNet is a lexical database that groups English words into sets of synonyms based on their meanings. These groups are called "synsets" and are linked together by semantic relationships such as antonyms, hypernyms, hyponyms, and meronyms. It is used in various applications of Natural Language Processing.
### What is SentiWordNet?
SentiWordNet is a lexical resource in natural language processing (NLP) that assigns sentiment scores to words. It assigns three scores to each word: positivity, negativity, and objectivity. These scores can be used to determine the overall sentiment of a text by summing the scores of the words it contains.
### What I learned from this assignment
I found fascinating how quickly you can get a sentiment or labeling for a piece of text. While not entirely accurate it was still impressive and can imagine how the implementation of the tools can be useful. I also saw how important context is when analyzying words since a word by itself doesn't hold an entire meaning. 
### Selected Sample output
```
Selected word: Hate

Synset 1:
Negative score =  0.375
Positive score =  0.125
Objective score =  0.5

Synset 2:
Negative score =  0.75
Positive score =  0.0
Objective score =  0.25
```
```
Synset: climb.v.01(go upward with gradual or continuous progress)  
	 Lemmas:['climb', 'climb_up', 'mount', 'go_up']
Synset: climb.v.02(move with difficulty, by grasping)  
	 Lemmas:['climb']
Synset: wax.v.02(go up or advance)  
	 Lemmas:['wax', 'mount', 'climb', 'rise']
Synset: climb.v.04(slope upward)  
	 Lemmas:['climb']
Synset: climb.v.05(improve one's social status)  
	 Lemmas:['climb']
Synset: rise.v.02(increase in value or to a higher point)  
	 Lemmas:['rise', 'go_up', 'climb']
```
### Link to the source code
You can find the full python notebook [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/03%20-%20Wordnet%20and%20SentiWordNet)
