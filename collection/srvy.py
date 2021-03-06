#!/usr/bin/python
import sys
import time
from time import sleep
from datetime import datetime
import random
import sqlite3
import csv
import ast
from configparser import ConfigParser
import setup_db

# VARIABLES
question_csv_location = '../archive/questions.csv'

sqlite_file = '../archive/srvy.db'

#Read Configuration File and set variables
parser = ConfigParser()
parser.read(r'../configuration/srvy.config')
keyboard = parser.get('advanced', 'keyboard')
screen_width= int(parser.get('screen', 'width'))
screen_height = int(parser.get('screen', 'height'))
background_color = ast.literal_eval(parser.get('colors', 'background_color'))
text_color = ast.literal_eval(parser.get('colors', 'text_color'))
question_interval = int(parser.get('questions', 'interval'))
question_font = parser.get('questions', 'font')

# Create database if it doesn't exist.
setup_db

# FUNCTIONS
def module_installed(module):
    if module in sys.modules:
        return True
    else:
        return False

def write_to_display(message, message_color, message_background):
    "takes a text variable and writes it to the display"
    text = font.render(message, True, message_color)
    screen.fill(message_background)
    screen.blit(text, (screen_width/2 - text.get_rect().width/2, screen_height/2)) #centers the text on the screen.
    pygame.display.flip()


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
        conn.commit()
        conn.close()
        write_to_display('Thank You!',(255,0,0),(255,255,255) )
        print("Successfully added response to database.")
        print("Thank you!")
        sleep(question_interval)
    except Exception as e:
        print(e)

    main()


def main():
    qs = random_questions()  # calls questions function that returns random question.
    if keyboard == True:
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
    else:
        if module_installed('gpiozero'):
            if module_installed('pygame'): #check to see if gpiozero is installed
                print(qs)
                write_to_display(qs, random.choice(text_color), random.choice(background_color))
                while True:

                    if like.is_pressed:
                        sleep(.5)
                        opinion = 1
                        add_response_to_database(qs, opinion)

                    elif dislike.is_pressed:
                        sleep(.5)
                        opinion = -1
                        add_response_to_database(qs, opinion)
            else:
                print('Pygame not installed')
                pass
        else:
            print('gpiozero is not installed.')
            pass # if you force gpiozero, but it's not installed it kicks you out.


if __name__ == '__main__':

    # Check if running on a Raspberry Pi

    try:
        from gpiozero import Button
        like = Button(26)
        dislike = Button(19)
        print('gpiozero installed.')
    except ImportError:
        print('gpiozero is not installed.')
        pass

    try:
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN) #remove pygame.FULLSCREEN for windowed mode
        pygame.mouse.set_visible(False) # Hides the mouse cursor
        font = pygame.font.SysFont("Futura, Helvetica, Arial", 48)
        print('pygame installed.')
    except ImportError:
        print('pygame is not installed.')
        pass

main()
