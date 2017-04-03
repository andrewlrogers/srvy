import pandas as pd
import time
from datetime import datetime, date
import csv
import random
import sqlite3
from random import randint


start_date = date(2014, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)

def pull_questions_from_csv():
    with open('synch/questions.csv', 'rU') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
        question=[]
        for row in readCSV:
            q = row[0]
            question.append(q)
        return(question)

def create_random_question():
    questions = pull_questions_from_csv()
    return(str(pull_questions_from_csv()[randint(0, len(questions)-1)]))

def add_random_questions_to_database():
    questions = [pull_questions_from_csv()]

    for date in date_range:
        daily_responses = []
        random_number_of_responses = randint(0, 10)

        # Don't add responses on a random number of days
        if random_number_of_responses == 0:
            continue

        count = 0
        # Create a random number of responses per day
        while count <= random_number_of_responses:
            random_hour = randint(10, 16) # Random hour between 10 AM and 5 PM
            random_minute = randint(0, 59)
            random_second = randint(0, 59)
            response_date = datetime(date.year, date.month, date.day, random_hour, random_minute, random_second)
            unix_response_date = time.mktime(response_date.timetuple())
            random_question = create_random_question()
            random_score = randint(0, 1)
            opinion = "Yes"

            if random_score == 0:
                opinion = "No"

            all_random_questions = (response_date, unix_response_date, random_question, random_score)
            daily_responses.append(all_random_questions)
            count += 1

        # Sort random daily responses by time "entered"
        daily_responses = sorted(daily_responses)
        count = 0

        # Add to database
        sqlite_file = 'srvy.db'
        table_name = 'responses'
        time_column = 'pythonDateTime'
        unix_time_column = 'unixTime'
        question_column = 'question'
        opinion_column = 'opinion'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        for response in daily_responses:
            try:
                c.execute('''INSERT INTO responses (pythonDateTime, unixTime, question, opinion) VALUES (?,?,?,?)''', (response[0], response[1], response[2], response[3]))
                print ("Successfully added response to database.")
            except Exception as e:
                print(e)
        conn.commit()
        conn.close


add_random_questions_to_database()
