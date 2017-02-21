#!/usr/bin/python
import leather
import csv
import sqlite3

with open('../export/test.csv') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)[:10]

    for row in data:
        row[0] = float(row[0]) if row[0] is not None else None

chart = leather.Chart('Data from CSV reader')
chart.add_bars(data)
chart.to_svg('../export/charts/simple_pairs.svg')


###########
from datetime import datetime, timedelta
import os

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

export_directory = '../export'
export_filename = 'srvy' + yesterday + '.csv'
full_export_path = os.path.join(export_directory, export_filename)

sqlite_file = '../srvy.db'
table_name = 'responses'

conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()

questions_from_yesterday = []

try:
    responses = c.execute("SELECT question FROM responses WHERE date = ?", (yesterday,))
    for response in responses:
        if response not in questions_from_yesterday:
            questions_from_yesterday.append(response)
except:
    pass


print(questions_from_yesterday)
