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

# SETUP VARIABLES

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

# Creates a dropbox object
dbx = dropbox.Dropbox(dropbox_token)


# FUNCTIONS

def download_questions():
    """downloads csv from dropbox and overwrites locally"""
    local = '../archive/questions.csv'  # The folder/file locally that we want the files to download to.
    with open(local, 'wb') as f:
        metadata, res = dbx.files_download('/questions.csv')
        f.write(res.content)


# MAIN

upload(files_to_upload)
