#!/usr/bin/python
import sys
import time
from time import sleep
from datetime import datetime
import random
import sqlite3
import csv
from configparser import ConfigParser

# VARIABLES
question_csv_location = '../archive/questions.csv'

sqlite_file = '../archive/srvy.db'


# FUNCTIONS


def module_installed(module):
    if module in sys.modules:
        return True
    else:
        return False


def get_current_questions(file_location):
    """Add each question from a text file to a list. Questions should be separated by newlines."""
    with open(file_location, 'r') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',', quotechar='"')
        questions = []
        for row in readCSV:
            if row:
                question = row[0]
                questions.append(question)
        return questions


def random_questions():
    """pulls returns a random question into main loop."""
    question = get_current_questions(question_csv_location)
    return random.choice(question)


def add_response_to_database(question, opinion):
    """Add response to SQLite 3 database"""

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    current_date = datetime.now()
    current_unix_time = time.time()

    try:
        c.execute('''INSERT INTO responses (pythonDateTime, unixTime, question, opinion) VALUES (?,?,?,?)''',
                  (current_date, current_unix_time, question, opinion))
        print("Successfully added response to database.")
        print("Thank you!")
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

    main()


def main():
    qs = random_questions()  # calls questions function that returns random question.
    print(qs)

    while True:

        opinion = input("Opinion [y/n]: ")

        if opinion == "y":
            sleep(.5)
            opinion = 1
            add_response_to_database(qs, opinion)

        elif opinion == "n":
            sleep(.5)
            opinion = -1
            add_response_to_database(qs, opinion)


if __name__ == '__main__':

    # Check if running on a Raspberry Pi

    try:
        from gpiozero import Button
    except ImportError:
        print("gpiozero is not installed.")
        pass

    try:
        import pygame
    except ImportError:
        print("pygame is not installed.")
        pass

    main()
