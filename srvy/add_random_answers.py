import pandas as pd
import time
from datetime import datetime, date
import csv
import sqlite3
from random import randint

start_date = date(2014, 1, 1)
end_date = datetime.now()
date_range = pd.date_range(start_date, end_date)


def pull_questions_from_csv():
    with open('synch/questions.csv', 'rU') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',', quotechar='|')
        question = []
        for row in readCSV:
            q = row[0]
            question.append(q)
        return (question)


def create_random_question():
    questions = pull_questions_from_csv()
    return (str(pull_questions_from_csv()[randint(0, len(questions) - 1)]))


def add_random_questions_to_database():

    for date in date_range:

        # Don't add any responses on Monday
        if date.dayofweek == 0:
            continue

        daily_responses = []
        random_number_of_responses = randint(0, 10)

        # Don't add responses on a random number of days
        if random_number_of_responses == 0:
            continue

        count = 0

        # Create a random number of responses per day
        while count <= random_number_of_responses:

            # If day is Thursday, record responses until 9 PM
            if date.dayofweek == 3:
                random_hour = randint(10, 20)
            # Record until 5 PM on all other days
            else:
                random_hour = randint(10, 16)

            random_minute = randint(0, 59)
            random_second = randint(0, 59)
            response_date = datetime(date.year, date.month, date.day, random_hour, random_minute, random_second)
            unix_response_date = time.mktime(response_date.timetuple())
            random_question = create_random_question()
            random_opinion = randint(0, 1)

            if random_opinion == 0:
                random_opinion = -1

            all_random_questions = (response_date, unix_response_date, random_question, random_opinion)
            daily_responses.append(all_random_questions)
            count += 1

        # Sort random daily responses by time "entered"
        daily_responses = sorted(daily_responses)

        # Add to database
        sqlite_file = 'srvy.db'

        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        for response in daily_responses:
            try:
                c.execute('''INSERT INTO responses (pythonDateTime, unixTime, question, opinion) VALUES (?,?,?,?)''',
                          (response[0], response[1], response[2], response[3]))
                print("Successfully added " + str(response[0]) + " to database.")
            except Exception as e:
                print(e)
        conn.commit()
        conn.close


add_random_questions_to_database()