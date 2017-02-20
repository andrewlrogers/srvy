#!/usr/bin/python
import sqlite3
import csv
from datetime import datetime

#reads from database and writes a new csv with responses from today.

current_date = str(datetime.now().strftime('%Y-%m-%d'))

destination_file = 'srvy' + current_date + '.csv' #names the csv with todays date
sqlite_file = 'srvy.db'
table_name = 'responses'


conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("SELECT * FROM responses WHERE date = ?", (current_date,))

csvWriter = csv.writer(open(destination_file, 'w'))
rows = c.fetchall()

for row in rows:
    csvWriter.writerow(row)
