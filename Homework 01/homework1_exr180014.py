# Homework 1 : Text Processing with Python
# Erik Rodriguez

import os
import pathlib
import pickle
import sys
import re


class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print('\nEmployee id: ' + self.id)
        print('\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t' + self.phone)


def process_data(input_text):
    person_dict = {}
    # clean each data field and add it to a dictionary
    for employee in input_text:
        tokens = employee.split(',')  # Last,First,Middle Initial,ID,Office phone
        last = tokens[0].capitalize()
        first = tokens[1].capitalize()
        middle = tokens[2].capitalize()
        if middle == '':
            middle = 'X'
        phone = process_phone(tokens[4])
        employee_id = process_employee_id(tokens[3], person_dict)

        curr_employee = Person(last, first, middle, employee_id, phone)
        person_dict[employee_id] = curr_employee

    return person_dict


def process_phone(input_text):
    phone = input_text
    while not (re.match(r"[0-9]{3}-[0-9]{3}-[0-9]{4}", phone)):
        phone = input(
            'The number ' + phone + ' isn\'t in the correct format \'123-456-7890\', please re-enter the number: ')
    return phone


def process_employee_id(input_text, employee_dict):
    employee_id = input_text.upper()
    flag = False
    while not flag:
        while not (re.match(r"([A-Z]{2}[0-9]{4})", employee_id)):
            employee_id = input(
                'The number ' + employee_id + ' isn\'t in the correct format \'XX1234\' , please re-enter the id: ')
            employee_id.upper()
        flag = True
        if employee_id in employee_dict:
            flag = False
            employee_id = input(
                'The ID ' + employee_id + ' is duplicated in the file, please enter a unique ID in \'XX1234\' format: ')
            employee_id.upper()
    return employee_id


if __name__ == '__main__':
    if not (len(sys.argv) == 2) or not (os.path.isfile(sys.argv[1])):
        print("Error: file path was not provided or it is not a valid filepath")
        quit()

    file_path = sys.argv[1]  # this is the relative path to the csv file
    with open(pathlib.Path.cwd().joinpath(file_path), 'r') as f:
        data = f.read().splitlines()

    employees = process_data(data[1:])  # ignoring the first line of text

    # pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # output employees
    print('\n\nEmployee list:')
    for emp_id in employees_in.keys():
        employees_in[emp_id].display()
