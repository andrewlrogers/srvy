import dropbox
import pathlib
import re

# the source file
folder = pathlib.Path(".")    # located in this folder
filename = "test.txt"         # file name
filepath = folder / filename  # path object, defining the file

# target location in Dropbox
target = "/Temp/"              # the target folder
targetfile = target + filename   # the target path and file name

# Create a dropbox object using an API v2 key
d = dropbox.Dropbox(your_api_access_token)

# open the file and upload it
with filepath.open("rb") as f:
   # upload gives you metadata about the file
   # we want to overwite any previous version of the file
   meta = d.files_upload(f.read(), targetfile, mode=dropbox.files.WriteMode("overwrite"))

