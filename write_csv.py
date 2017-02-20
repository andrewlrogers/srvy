"""Export all responses from yesterday and save them to a CSV file."""

import sqlite3
import csv
from datetime import datetime, timedelta
import os


today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

export_directory = 'export'
export_filename = 'srvy' + yesterday + '.csv'
full_export_path = os.path.join(export_directory, export_filename)

sqlite_file = 'srvy.db'
table_name = 'responses'
date_column = 'date'
time_column = 'time'
score_column = 'score'
question_column = 'question'


conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()


#c.execute("SELECT * FROM responses WHERE date LIKE '%"+ current_date +"%'")

c.execute("SELECT * FROM responses WHERE date = ?", (yesterday,))

csvWriter = csv.writer(open(full_export_path, 'w'))
rows = c.fetchall()

for row in rows:
    csvWriter.writerow(row)

