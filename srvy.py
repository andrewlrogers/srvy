from gpiozero import Button
from time import sleep
from datetime import datetime
import random
import sqlite3
import pygame
import csv


#Pygame Setup
pygame.init()

screen_width=800 #Set width and height to match your monitor.
screen_height=480
bg_color = [(105, 58, 119), (162, 173, 0), (125, 154, 170), (86, 90,92)] #crocker colors

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN) #remove pygame.FULLSCREEN for windowed mode
pygame.mouse.set_visible(False) # Hides the mouse cursor

font = pygame.font.SysFont("Futura, Helvetica, Arial", 48) #system fonts and size


#Button Setup
like = Button(18)
okay = Button(14)
dislike = Button(15)

def pull_qs_from_csv(): #reads the questions into mem from csv in case they have been updated.
    with open('questions.csv', 'rU') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
        question=[]
        for row in readCSV:
            q = row[0]
            question.append(q)
        return question

def random_questions(): #pulls returns a random question into main loop.
    return random.choice(question)

def add_response_to_database(score, question):
    """Add response to SQLite 3 database"""

    sqlite_file = 'srvy.db'
    table_name = 'responses'
    date_column = 'date'
    time_column = 'time'
    score_column = 'score'
    question_column = 'question'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    try:
        c.execute('''INSERT INTO responses (date, time, score, question) VALUES (?,?,?,?)''', (current_date, current_time, score, question))
        print ("Successfully added response to database.")
	    text = font.render('Thank You!', True, (255, 255, 255)) #text to display and color in tuple
        screen.fill((105, 58, 119)) #sets background color
        screen.blit(text, (screen_width/2 - text.get_rect().width/2,screen_height/2)) #adds text to center of screen
        pygame.display.flip()
        sleep(2) #gives viewer a chance to read
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

    main()

def main():
    qs = random_questions() #calls questions function that returns random question.

    text = font.render(qs, True, (255, 255, 255)) #displays text, anti-aliasing  and sets text color
    screen.fill(random.choice(bg_color)) #sets background color
    screen.blit(text, (screen_width/2 - text.get_rect().width/2,screen_height/2)) #adds text to screen and centers
    pygame.display.flip()

    while True:
        if like.is_pressed:
            score = 2
            sleep(.5)
            add_response_to_database(score, qs)

        elif okay.is_pressed:
            score = 1
            sleep(.5)
            add_response_to_database(score, qs)

        elif dislike.is_pressed:
            score = 0
            sleep(.5)
            add_response_to_database(score, qs)


question = pull_qs_from_csv()
main()
