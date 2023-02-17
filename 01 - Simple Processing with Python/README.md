# Assignment #1 : Simple Text Processing with Python 🐍
The goal of the following program is to get comfortable with Python. In this assignment, we take a CSV file as input that contains information such as names, IDs, and phone numbers. Using various functions we sanitize the data and print it to the console. 

### How to run
To run the program you must:
- locate the path of the CSV file you will use then you will pass the path as an argument to the program
- Have Python 3.6 or higher to run
```
 python3 simple-processing.py data/data.csv
```
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
