<p align="center">
  <img src="https://mir-s3-cdn-cf.behance.net/project_modules/1400/0a885470672999.5bf66d0789749.png" />
</p>

# Natural Language Processing Portfolio 🗣️

## About Me 👨‍💻
Hello reader, my name is Erik and I would like to welcome you to my Natural Language Processing Portfolio. In this collection, I have compiled my first projects in the field of natural language processing, where I explore the different techniques and tools used to process, analyze and generate human language data. As a novice in this field, I am excited to share my learning journey and showcase the skills I have acquired so far. <br>

In addition to my technical skills in natural language processing, I possess strong soft skills that allow me to excel in any work environment. I am a skilled problem-solver who can approach challenges from multiple perspectives to find the best possible solution. Furthermore, I have experience working in both team-oriented and independent environments, and am able to adapt to any situation with ease. I possess excellent communication skills that allow me to articulate complex ideas and work collaboratively with others. My time management and project management skills ensure that I am able to complete tasks efficiently and effectively. <br>

Through these projects, I aim to demonstrate not only my technical abilities in natural language processing, but also my soft skills, which are essential to any workplace. Thank you for visiting my portfolio. <br>


## Works Index 👈
As I reflect on my learning experience in Natural Language Processing, I am happy with the outcomes of my projects and the skills I have acquired. I am excited to take these skills with me as I explore further personal projects and continue to expand my knowledge in this rapidly changing field. In the future, I plan to stay up to date with the latest NLP techniques and tools by reading research papers and participating in online forums. I am enthusiastic about the possibilities that this field offers and I am open to potential employment opportunities where I can apply my skills and contribute to the development of innovative NLP solutions.<br>

Click on the link to navigate to my works. <br>

[Part 0: Overview of NLP](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#overview-of-natural-language-processing)<br>
[Part 1: Simple Processing with Python](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-1--simple-text-processing-with-python-) <br>
[Part 2: Word Guess Game](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-2--word-guess-game-) <br>
[Part 3: WordNet and SentiWordNet](https://github.com/Tarzerk/NLP-Portfolio/blob/master/README.md#assignment-3-wordnet-and-sentiwordnet-)  <br>
[Part 4: N-grams](https://github.com/Tarzerk/NLP-Portfolio/tree/master/04%20-%20Ngrams) <br>
[Part 5: Sentence Parsing](https://github.com/Tarzerk/NLP-Portfolio/blob/master/05%20-%20Sentence%20Parsing/Sentence_Parsing.pdf)<br>
[Part 6: Webcrawler](https://github.com/Tarzerk/NLP-Portfolio#part-6-webcrawler-%EF%B8%8F)<br>
[Part 7: Text Classification](https://github.com/Tarzerk/NLP-Portfolio#part-7-text-clasification-)<br>
[Part 8: ACL Research Paper](https://github.com/Tarzerk/NLP-Portfolio#part-8-acl-research-paper-%EF%B8%8F)<br>
[Part 9: Chatbot](https://github.com/Tarzerk/NLP-Portfolio#part-9-chatbot-)<br>

## Part 0: Overview of Natural Language Processing ✈️
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

## Part 1: Simple Text Processing with Python 🐍
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

## Part 2: Word Guess Game 🤔
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
........

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

....

Your current score is: 10
connecti_e
Enter a letter to guess: v
Right!

You got it!! The word was connective

Game over, your total score is: 11
```
### What I learned with this assignment
I learned how powerful the Natural Language Took Kit (NLTK) library is. It was able to minimize the amount of code since a lot of
the post processing can be done in just a few lines of code. I also saw how some things might seem inconsistent thereofore it is important to clean up
the data a bit. 
### Link to the source code
You can find the link to the source code as well as the sample text I used by clicking [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/02%20-%20Word%20Guess%20Game%20with%20NLTK)

## Part 3: Wordnet and SentiWordNet 🔠
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

## Part 4: Ngrams 🦊

N-grams are contiguous sequences of n items from a given text or speech. In natural language processing (NLP), these items are typically words, but they can also be characters, syllables, or other units of language.

For example, if we consider the sentence "The quick brown fox jumps over the lazy dog," we can generate the following n-grams:

```
Unigrams (n=1): [The], [quick], [brown], [fox], [jumps], [over], [the], [lazy], [dog]
Bigrams (n=2): [The quick], [quick brown], [brown fox], [fox jumps], [jumps over], [over the], [the lazy], [lazy dog]
Trigrams (n=3): [The quick brown], [quick brown fox], [brown fox jumps], [fox jumps over], [jumps over the], [over the lazy], [the lazy dog]
N-grams are commonly used in NLP tasks such as language modeling, where they are used to estimate the probability of a word given its context. For example, by analyzing the frequency of bigrams in a large corpus of text, we can estimate the probability of a particular word following another word in a sentence.
```
N-grams can also be used in tasks such as text classification, information retrieval, and machine translation.
In this assignment, I worked with Arielle (posadari) to explore how we can use N-grams to classify texts

## Part 5: Parsing Sentences 📈
In this assignment, in this assignment we explored different methods of parsing sentences.
### PSG Graphs:
PSG (Phrase Structure Grammar) Graphs are a type of syntactic structure that represents the hierarchical relationships between words and phrases in a sentence. In PSG graphs, the words and phrases are organized into a tree-like structure, with each node representing a constituent or a word, and the branches representing the relationships between the constituents. PSG graphs are commonly used in natural language processing (NLP) to parse sentences and extract syntactic information from text.

### SRL Graphs:
SRL (Semantic Role Labeling) Graphs are a type of graph that represents the semantic relationships between the words in a sentence. SRL graphs represent the roles played by each word in the sentence, such as the agent, patient, instrument, or location of an action. SRL graphs are commonly used in NLP to extract semantic information from text, such as in question answering or information extraction tasks.

### Dependency Graphs:
Dependency Graphs are a type of syntactic structure that represents the dependencies between words in a sentence. In a dependency graph, each word is represented as a node, and the relationships between the words are represented as directed edges. The edges represent the grammatical relationships between the words, such as subject-verb or modifier-noun relationships. Dependency graphs are commonly used in NLP for parsing and syntactic analysis of sentences.

## Part 6: WebCrawler 🕷️
Web crawlers start by visiting a web page, then follow the links on that page to other pages, and continue to recursively crawl and index new pages as they discover them. In this assignment, I collaborated with Arielle Posadas (posadari) to explore how to scrap website and use the
tf-idf algorithm to get relevant information. 

### Link to our work
You can find the report and our code listed [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/06%20-%20Webcrawler)

## Part 7: Text Classification ⚽️
<p align="center">
  <img src="https://media.tenor.com/rAnOhr5xiUgAAAAd/messi-world-cup.gif" alt="Messi World Cup" />
</p>

<p align="center">
  <img src="https://media.tenor.com/IkMW3tmJo6wAAAAd/messi-world-cup.gif" alt="Elden Ring Character" />
</p>
In this assignment, I took a FIFA World Cup data set and used various algorithms, including Naive Bayes and Neural Networks, to perform sentiment analysis. Before applying these techniques, I had to preprocess the data, which included cleaning up the tweets to make the analysis possible. By applying NLP techniques and using these algorithms, I was able to gain insights into the sentiments expressed by fans during the World Cup. The combination of these techniques allowed me to accurately classify the tweets as positive, negative, or neutral sentiments, and enabled me to draw conclusions about the overall sentiment of fans during the tournament.

### Link to the source code
You can find the report and code [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/07%20-%20Text%20Classification)

## Part 8: ACL research paper 🗞️
In this assignment, Arielle Posadas (posadari) and I analyzed the paper "Which side are you on? Insider-Outsider classification in conspiracy-theoretic social media," which was submitted to the 2022 ACL conference. The gist of the paper was to explore how natural language processing techniques can be used to classify texts related to conspiracy theories as either supporting or opposing a given theory. By applying various NLP techniques, including language modeling and sentiment analysis, the authors were able to identify features of texts that were indicative of their stance towards a conspiracy theory. Our analysis of the paper allowed us to gain insights into the potential of NLP techniques in identifying and classifying texts related to conspiracy theories, which is an important issue in today's world. Overall, our analysis of the paper highlighted the importance of NLP in addressing real-world problems and demonstrated the potential for further research in this area.

### Link to our work
You can find the link to the summary is [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/08%20-%20ACL%20research%20paper)

## Part 9: ChatBot 🤖
<p align="center">
  <img src="https://media.tenor.com/N9zIBaaY-TgAAAAd/elden-ring-malenia.gif" alt="Elden Ring Character" />
</p>

In this assignment, we combined all of the NLP techniques we had learned up to that point to create a chatbot that was based on the popular video game, Elden Ring. The chatbot, which we named EldenBot, was designed to interact with users in a conversational manner, using natural language processing techniques to understand and respond to user queries related to the game. To build the chatbot, we used a combination of techniques such as named entity recognition and language modeling. By integrating these techniques, we were able to create a chatbot that was able to understand the context of user queries and provide appropriate responses. EldenBot was a great way for us to apply our NLP skills to a real-world project and we were thrilled with the results. You can check out EldenBot to see how it works and experience the benefits of NLP in action.

### Link to the source code
You can try the bot for yourself [here](https://github.com/Tarzerk/NLP-Portfolio/tree/master/09%20-%20Chatbot)

