#!/usr/bin/python
import leather
import csv
import sqlite3


###########
from datetime import datetime, timedelta
import os

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

export_directory = 'export'
export_filename = 'srvy' + yesterday + '.csv'
full_export_path = os.path.join("../", export_directory, export_filename) 
sqlite_file = os.path.join("../", 'srvy.db')
table_name = 'responses'

conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()


# Create list of questions from yesterday
questions_from_yesterday = []

try:
    responses = c.execute("SELECT question FROM responses WHERE date = ?", (yesterday,))
    for response in responses:
        if response not in questions_from_yesterday:
            questions_from_yesterday.append(response)
except:
    pass

# Create chart with breakdown of scores for one question from yesterday
score_breakdown = []

try:
    # Loop through 3 times, since there are 3 possible scores
    i = 0
    while i != 3:
        pud = c.execute("SELECT CAST(score as text), COUNT(score)FROM responses WHERE date = ? and question = ? and score = ?", (yesterday, questions_from_yesterday[0][0], i))
        for response in pud:
            score_breakdown.append(response)
        i = i+1
except:
    pass

chart = leather.Chart(questions_from_yesterday[0][0])
chart.add_columns(score_breakdown)
chart.to_svg(os.path.join("../", 'export/charts/yesterday_question.svg'))
