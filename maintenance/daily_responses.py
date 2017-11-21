#!/usr/bin/python
"""Export all responses from yesterday and save them to a .csv file."""

import sqlite3
import csv
from datetime import datetime, timedelta
import os
import time


today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

now_datetime = time.mktime((datetime.now()).timetuple()) #returns the dateime as a timestamp
prev_datetime = time.mktime((datetime.now() - timedelta(days=1)).timetuple())

## SQLITE3 VARIABLES
sqlite_query = 'SELECT * FROM responses WHERE unixTime BETWEEN ' + str(today) + ' AND ' + str(yesterday) + ' '


export_directory = '../archive'
export_filename = yesterday + '_responses' + '.csv'
full_export_path = os.path.join(export_directory, export_filename)

sqlite_file = '../archive/srvy.db'
table_name = 'responses'


conn =  sqlite3.connect(sqlite_file)
c = conn.cursor()

#c.execute("SELECT * FROM responses WHERE date LIKE '%"+ current_date +"%'")

try:
    c.execute(sqlite_query)
    csvWriter = csv.writer(open(full_export_path, 'w'))
    rows = c.fetchall()

    for row in rows:
        csvWriter.writerow(row)
except:
    pass
