#!/usr/bin/python
"""Export all responses from yesterday and save them to a .csv file."""

import sqlite3
import csv
from datetime import datetime, timedelta
import os
import time

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

today_timestamp = datetime.now().timestamp()  # returns the dateime as a timestamp
yesterday_timestamp = (datetime.now() - timedelta(days=1)).timestamp()

## SQLITE3 VARIABLES
sqlite_query = 'SELECT response_key, pythonDateTime, question, opinion FROM responses WHERE unixTime BETWEEN ' + str(
    yesterday_timestamp) + ' AND ' + str(today_timestamp) + ' '

export_directory = '../archive'
export_filename = yesterday + '_responses' + '.csv'
full_export_path = os.path.join(export_directory, export_filename)

sqlite_file = '../archive/srvy.db'
table_name = 'responses'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

try:
    c.execute(sqlite_query)
    headers = [row[0] for row in c.description]
    csvWriter = csv.writer(open(full_export_path, 'w'))
    rows = c.fetchall()

    csvWriter.writerow(headers)

    for row in rows:
        csvWriter.writerow(row)
except:
    pass
