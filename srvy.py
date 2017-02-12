from gpiozero import Button
from time import sleep
from datetime import datetime
import random
import sqlite3
from signal import pause

print('initializing variables')
like = Button(18)
okay = Button(14)
dislike = Button(15)

questions = ['Did you enjoy your visit today?', 'Would you reccomend us to a friend?', 'Were you satisfied with the service you received today', 'Were you able to find what you were looking for?']

#pull questions from csv file on dropbox, run daily at midnight. From a different script. Q's stored as CSV.

def add_response_to_database():
    """Add response to SQLite 3 database"""

    sqlite_file = 'srvy.db'
    table_name = 'responses'
    date_column = 'date'
    time_column = 'time'
    score_column = 'score'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')

    try:
        c.execute('''INSERT INTO responses (date, time, score) VALUES (?,?,?)''', (current_date, current_time, score))
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

def main():

    qs = random.choice(questions)

    print(qs)

    while True:
        if like.is_pressed:
            score = 2 
            sleep(.5)
            add_response_to_database()
            
        elif okay.is_pressed: 
            score = 1
            sleep(.5)
            add_response_to_database()

        elif dislike.is_pressed:
            score = 0
            sleep(.5)
            add_response_to_database()

main()

