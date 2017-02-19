import sqlite3
import csv
from datetime import datetime

destination_file = 'srvy.csv'
sqlite_file = 'srvy.db'
table_name = 'responses'
date_column = 'date'
time_column = 'time'
score_column = 'score'
question_column = 'question'

current_date = datetime.now().strftime('%Y-%m-%d')

conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()


survey  = c.execute("SELECT * FROM responses WHERE date LIKE '%2017-02-18%';")

print(c.fetchall())

#for row in rows:
#    c.execute('SELECT * FROM responses')
#    csvWriter.writerows(rows)

