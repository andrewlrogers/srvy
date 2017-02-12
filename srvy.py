from gpiozero import Button
from time import sleep
from datetime import datetime
import random
import sqlite3
from signal import pause

# print('initializing variables')
# like = Button(18)
# okay = Button(14)
# dislike = Button(15)
questions = ['Did you enjoy your visit today?', 'Would you reccomend us to a friend?', 'Were you satisfied with the service you received today', 'Were you able to find what you were looking for?']
#pull questions from csv file on dropbox, run daily at midnight. From a different script. Q's stored as CSV.

def liked():
    print('Like')
    score = 2
    sleep(.5) #prevents multiple presses
    #add time, qs, and score to db
    return(score)

def okayed(score, qs, responses):
    print('I dont really care')
    score = 1
    sleep(.5)
    return(score)

def disliked(score, qs, responses):
    print('I hate life')
    score = 0
    sleep(.5)
    return(score)

def main():
    sqlite_file = 'srvy.db'
    table_name = 'responses'
    date_column = 'date'
    time_column = 'time'
    score_column = 'score'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    qs = random.choice(questions)

#    # Physical buttons
#    print(qs)
#    while True:
#        if like.is_pressed:
#            liked()
#        elif okay.is_pressed: 
#            okayed()
#        elif dislike.is_pressed:
#            disliked()

    # Virtual buttons
    current_date = datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.now().strftime('%H:%M:%S')
    score = 2
    try:
        c.execute('''INSERT INTO responses (date, time, score) VALUES (?,?,?)''', (current_date, current_time, score))
            
    except Exception as e:
        print(e)

    conn.commit()
    conn.close()

main()

