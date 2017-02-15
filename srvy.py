from gpiozero import Button
from time import sleep
from datetime import datetime
import random
import sqlite3
import pygame


#Pygame Setup
pygame.init()
screen_width=1440 #Set width and height to match your monitor.
screen_height=900
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False) # Hides the mouse cursor

done = False
font = pygame.font.SysFont("Futura, Helvetica, Arial", 48) #system fonts and size
text = font.render(qs, True, (255,255,255)) #text, anti-alias, color

#Button Setup
like = Button(18)
okay = Button(14)
dislike = Button(15)

qs = random.choice(['Did you enjoy your visit today?', 'Would you reccomend us to a friend?', 'Were you satisfied with the service you received today', 'Were you able to find what you were looking for?'])
bg_color = random.choice([(105, 58, 119), (162, 173, 0), (125, 154, 170), (86, 90,92)]) #crocker colors

#pull questions from csv file on dropbox, run daily at midnight. From a different script. Q's stored as CSV.

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
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()
    main()

def main():
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

            screen.fill(bg_color) #sets background color
            screen.blit(text, (screen_width/2 - text.get_rect().width/2,screen_height/2)) #adds text to
            pygame.display.flip()
            
        if like.is_pressed:
            score = 2
            question = qs
            sleep(.5)
            add_response_to_database(score, question)

        elif okay.is_pressed:
            score = 1
            question = qs
            sleep(.5)
            add_response_to_database(score, question)

        elif dislike.is_pressed:
            score = 0
            question = qs
            sleep(.5)
            add_response_to_database(score, question)

main()
