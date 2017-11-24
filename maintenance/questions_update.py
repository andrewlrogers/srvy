#!/usr/bin/python

""" Downloads questions from dropbox to be integrated into srvy """

import dropbox
import pathlib
from datetime import datetime, timedelta
from configparser import ConfigParser

# Dropbox Configuration
parser = ConfigParser()
parser.read('../configuration/srvy.config')
dropbox_token = parser.get('dropbox', 'token')

""" S E T U P _ V A R I A B L E S """

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

# Creates a dropbox object
dbx = dropbox.Dropbox(dropbox_token)

""" D O W N L O A D I N G _ FUNCTIONS """


def download_questions():
    """downloads csv from dropbox and overwrites locally"""
    local = '../archive/questions.csv'  # The folder/file locally that we want the files to download to.
    with open(local, 'wb') as f:
        metadata, res = dbx.files_download('/questions.csv')
        f.write(res.content)


""" U P L O A D I N G _ FUNCTIONS"""

# the source files to upload
csv_to_upload = str(yesterday) + "_responses.csv"
files_to_upload = (csv_to_upload)


def upload(files_to_upload):  # need to change this function name
    for f in files_to_upload:
        try:
            filepath = pathlib.Path("../archive/" + f)
            print(f, filepath)
            upload_files(filepath, f)
            print('passed ' + f)
        except IOError:
            print('No such file')


def upload_files(filepath, filename):
    # open the file and upload it
    target = "/"
    with filepath.open("rb") as f:
        # upload gives you metadata about the file
        # we want to overwite any previous version of the file
        try:
            targetfile = target + filename
            meta = dbx.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))
        except IOError:
            print('No such file')


""" M A I N """
download_questions()
upload(files_to_upload)
# upload_files(pathlib.Path("/home/pi/srvy/export/srvy2017-02-18.csv"), "srvy2017-02-18.csv")
