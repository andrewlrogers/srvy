#!/usr/bin/python

""" Downloads questions from dropbox to be integrated into srvy """

import dropbox

access_token = "I4gEG90KcJAAAAAAAAACORywbA7QoPUArtQGf0TstZFTmkIsDTrLksBSIGBHKD8I"

dbx = dropbox.Dropbox(access_token)

local = '/home/pi/srvy/synch/questions.csv'

with open (local, 'w') as f:
    metadata, res = dbx.files_download('/questions.csv')
    f.write(res.content)
