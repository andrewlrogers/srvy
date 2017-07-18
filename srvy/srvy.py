#!/usr/bin/python
import sys

try:
    from gpiozero import Button
except ImportError:
    print("gpiozero is not installed.")
    pass

import time
from time import sleep
from datetime import datetime
import random
import sqlite3

try:
    import pygame
except ImportError:
    print("pygame is not installed.")
    pass

import csv
from configparser import ConfigParser


def module_installed(module):
    if module in sys.modules:
        return True
    else:
        return False


def pull_qs_from_csv(file_location):  # reads the questions into mem from csv in case they have been updated.
    with open(file_location, 'rU') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',', quotechar='|')
        question = []
        for row in readCSV:
            q = row[0]
            question.append(q)
        return question


def random_questions():  # pulls returns a random question into main loop.
    return random.choice(question)


def add_response_to_database(question, opinion):
    """Add response to SQLite 3 database"""

    sqlite_file = 'srvy.db'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    current_date = datetime.now()
    current_unix_time = time.clock()

    try:
        c.execute('''INSERT INTO responses (pythonDateTime, unixTime, question, opinion) VALUES (?,?,?,?)''',
                  (current_date, current_unix_time, question, opinion))
        print("Successfully added response to database.")
        if module_installed('pygame'):
            text = font.render('Thank You!', True, (255, 255, 255))  # text to display and color in tuple
            screen.fill((105, 58, 119))  # sets background color
            screen.blit(text,
                        (screen_width / 2 - text.get_rect().width / 2,
                         screen_height / 2))  # adds text to center of screen
            pygame.display.flip()
            sleep(2)  # gives viewer a chance to read
        else:
            print("Thank you!")
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

    main()


def main():
    qs = random_questions()  # calls questions function that returns random question.
    print(qs)

    pygame_installed = module_installed('pygame')

    if pygame_installed:
        text = font.render(qs, True, (255, 255, 255))  # displays text, anti-aliasing  and sets text color
        screen.fill(random.choice(bg_color))  # sets background color
        screen.blit(text,
                    (
                    screen_width / 2 - text.get_rect().width / 2, screen_height / 2))  # adds text to screen and centers
        pygame.display.flip()
    else:
        pass

    while True:

        opinion = input("Opinion: ")

        if pygame_installed:
            if like.is_pressed:
                sleep(.5)
                opinion = 1
                add_response_to_database(qs, opinion)

            elif dislike.is_pressed or opinion == -1:
                sleep(.5)
                opinion = -1
                add_response_to_database(qs, opinion)

        else:

            if opinion == "1":
                sleep(.5)
                opinion = 1
                add_response_to_database(qs, opinion)

            elif opinion == "-1":
                sleep(.5)
                opinion = -1
                add_response_to_database(qs, opinion)

if __name__ == '__main__':

    # Configuration
    parser = ConfigParser()
    parser.read('srvy.config', encoding='utf-8')
    screen_width = parser.get('screen', 'width')
    screen_height = parser.get('screen', 'height')

    if module_installed('pygame'):
        # Pygame Setup
        pygame.init()

        screen_width = 800  # Set width and height to match your monitor.
        screen_height = 480
        bg_color = [(105, 58, 119), (162, 173, 0), (125, 154, 170), (86, 90, 92)]  # crocker colors

        screen = pygame.display.set_mode((screen_width, screen_height),
                                         pygame.FULLSCREEN)  # remove pygame.FULLSCREEN for windowed mode
        pygame.mouse.set_visible(False)  # Hides the mouse cursor

        font = pygame.font.SysFont("Futura, Helvetica, Arial", 48)  # system fonts and size

        # Button Setup
        love = Button(18)
        like = Button(14)
        dislike = Button(15)
        hate = Button(17)

    else:
        pass

    question = pull_qs_from_csv('synch/questions.csv')
    main()
