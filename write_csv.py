import sqlite3
import csv
from datetime import datetime


current_date = datetime.now().strftime('%Y-%m-%d')

destination_file = 'srvy' + current_date + '.csv'
sqlite_file = 'srvy.db'
table_name = 'responses'
date_column = 'date'
time_column = 'time'
score_column = 'score'
question_column = 'question'


conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()


c.execute("SELECT * FROM responses WHERE date LIKE '%"+ current_date +"%'")

csvWriter = csv.writer(open(destination_file, 'w'))
rows = c.fetchall()

for row in rows:
    csvWriter.writerow(row)

