#!/usr/bin/python
"""Export all responses from yesterday and save them to a .csv file."""

import sqlite3
import csv
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

#c.execute("SELECT * FROM responses WHERE date LIKE '%"+ current_date +"%'")

try:
    c.execute("SELECT * FROM responses WHERE date = ?", (yesterday,))
    csvWriter = csv.writer(open(full_export_path, 'w'))
    rows = c.fetchall()

    for row in rows:
        csvWriter.writerow(row)
except:
    pass
