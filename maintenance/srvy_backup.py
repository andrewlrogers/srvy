#!/usr/bin/python

""" places the most recent datetime_responses.csv on to remote dropbox location and overwrites remote srvy.db with local srvy.db """

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


""" U P L O A D I N G _ FUNCTIONS"""

# the source files to upload
csv_to_upload = str(yesterday) + "_responses.csv"
files_to_upload = (csv_to_upload, "srvy.db")


def upload(files_to_upload):  # need to change this function name
    for f in files_to_upload:
        try:
            filepath = pathlib.Path("../archive/" + f)
            print(f, filepath)
            upload_files(filepath, f)
            print('passed ' + f)
        except IOError:
            print('No such file: ' + f)


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
upload(files_to_upload)
# upload_files(pathlib.Path("/home/pi/srvy/export/srvy2017-02-18.csv"), "srvy2017-02-18.csv")
