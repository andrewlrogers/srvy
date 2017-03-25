#!/usr/bin/python

""" Downloads questions from dropbox to be integrated into srvy """
""" Uploads charts and csv's"""

import dropbox
import pathlib
import re
from datetime import datetime, timedelta


""" S E T U P _ V A R I A B L E S """

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
#You will need to generate your own access token for dropbox
access_token = "I4gEG90KcJAAAAAAAAACORywbA7QoPUArtQGf0TstZFTmkIsDTrLksBSIGBHKD8I"
#Creates a dropbox object
dbx = dropbox.Dropbox(access_token)

""" D O W N L O A D I N G _ FUNCTIONS """

def download_questions():
    local = '/home/pi/srvy/synch/questions.csv'#The folder/file locally that we want the files to download to.
    with open (local, 'w') as f:
        metadata, res = dbx.files_download('/questions.csv')
        f.write(res.content)


""" U P L O A D I N G _ FUNCTIONS"""

# the source files to upload
chart_to_upload= yesterday + ".html"
csv_to_upload = yesterday + ".csv"
files_to_upload = (chart_to_upload, csv_to_upload)

def foopa(files_to_upload): #need to change this function name
    for f in files_to_upload:
        filepath = pathlib.Path("/home/pi/srvy/export/" + f)  
        upload_files(filepath, f)

def upload_files(filepath, filename):
    # open the file and upload it
    target = "responses/"
    with filepath.open("rb") as f:
        # upload gives you metadata about the file
        # we want to overwite any previous version of the file
        targetfile = target + filename
        meta = dbx.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))

""" M A I N """
download_questions()
foopa(files_to_upload)
