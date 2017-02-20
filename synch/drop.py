#!/usr/bin/python
import dropbox

access_token = "I4gEG90KcJAAAAAAAAACORywbA7QoPUArtQGf0TstZFTmkIsDTrLksBSIGBHKD8I"

dbx = dropbox.Dropbox(access_token)

local = '/home/pi/srvy/questions.csv'

with open (local, 'w') as f:
    metadata, res = dbx.files_download('/questions.csv')
    f.write(res.content)
