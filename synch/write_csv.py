<<<<<<< HEAD:synch/write_csv.py
#!/usr/bin/python
=======
"""Export all responses from yesterday and save them to a .csv file."""

>>>>>>> csv:write_csv.py
import sqlite3
import csv
from datetime import datetime, timedelta
import os


<<<<<<< HEAD:synch/write_csv.py
#reads from database and writes a new csv with responses from today.
=======
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
>>>>>>> csv:write_csv.py

export_directory = 'export'
export_filename = 'srvy' + yesterday + '.csv'
full_export_path = os.path.join(export_directory, export_filename)

<<<<<<< HEAD:synch/write_csv.py
destination_file = 'srvy' + current_date + '.csv' #names the csv with todays date
=======
>>>>>>> csv:write_csv.py
sqlite_file = 'srvy.db'
table_name = 'responses'


conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()

<<<<<<< HEAD:synch/write_csv.py
c.execute("SELECT * FROM responses WHERE date = ?", (current_date,))

csvWriter = csv.writer(open(destination_file, 'w'))
rows = c.fetchall()

for row in rows:
    csvWriter.writerow(row)
=======

#c.execute("SELECT * FROM responses WHERE date LIKE '%"+ current_date +"%'")

try:
    c.execute("SELECT * FROM responses WHERE date = ?", (yesterday,))
    csvWriter = csv.writer(open(full_export_path, 'w'))
    rows = c.fetchall()

    for row in rows:
        csvWriter.writerow(row)
except:
    pass

>>>>>>> csv:write_csv.py
