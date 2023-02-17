# Word Guess Game with NLTK
## How to run
```
python3 word-guess.py ana19.txt
```
## Sample output
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
