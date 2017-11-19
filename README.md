# SRVY
## A Physical Like/Dislike Questionnaire for Non-Profits
===
---


## Overview / Functionality
SRVY uses a screen to pose a visitor a question and then records their response using two physical buttons that correspond to two different values (Like, Dislike). The response is recorded in a SQLite3 database. On a daily basis SRVY generates a series of charts and reports which are automatically uploaded to a Dropbox application. Questions can be appended on a daily basis by editing a .CSV file also located in the Dropbox account.

The intended audience is smaller art non-profits such as museums, theaters, and community art centers. The goal is to provide a low-cost and customizable tool that will allow organizations to track audience engagement and determine metrics of success with little daily upkeep.



### Archive

- questions.csv - The questions asked in srvy.py updated nightly with questions_update.py
- srvy.db - The sqlite3 database that houses all of the responses from srvy.py
- datetime_responses.csv - a collection of csv files with responses from different datetimes.

### Collection

- Srvy.py - Displays a question from a csv file and records user response to sqlite db
  - Unpack questions from questions.csv and create a list
  - Display a random question on to screen from list
  - Be prepared to collect input
    - If pressed
      - Record response from physical button input
        - date and time
          - mm/dd/yyyy HH:MM:SS
          - Unix time
        - Question
        - Opinion
      - Display Thank You text
        - Rest interval
      - Return to collecting input

### Configuration

- Readme.md - information on initial configuration
  - Running setup.py to create srvy.db
  - Steps for tweaking srvy.py
  - Steps for hardware setup
  - Steps for creating back-up chrontab.

- Srvy.config - sets global configuration variables on
  - Dropbox API
  - Screen size
  - Palette
  - Typeface
  - Sqlite file
  - GPIO pins for button input
    - Have set to defaults

- Setup.py - Initializes the sqlite.db file and includes the schema

- example.srvy.config - an example configuration file

### Maintenance
- Questions_update.py - overwrites local questions.csv nightly from remote Dropbox file
  - Run nightly by crontab
  - Connect to Dropbox
  - Download questions.csv from dropbox
  - Overwrite local version of questions.csv

- daily_responses.py - creates a datetime_responses.csv file with the responses from yesterday.
  - Run by crontab
  - Set date range for collecting responses
    - Timedelta
  - Connect to srvy.db with sqlite3
  - Write responses to csv file (maybe hourly instead of daily, in case power is shut off)
  - Save csv as datetime_responses.csv in archive directory

- Monthly_responses.py - nearly identical to daily_responses, but with a monthly timedelta

- Srvy_backup.py - places the most recent datetime_responses.csv on to remote dropbox location and overwrites remote srvy.db with local srvy.db

## Requirements
### Hardware
### Packages

## Installation
### Config file
1. Find the file **srvy.config.example**. Rename it **srvy.config**.

### Dropbox
1. Open **srvy.config** in a text editor.
2. Find the [dropbox] section:

            [dropbox]
            token = INSERT_DROPBOX_TOKEN_HERE

3. Replace INSERT_DROPBOX_TOKEN_HERE with your private Dropbox token.
4. Save **srvy.config**

### Customization

### Possible Future Functionality

- Add support for C.H.I.P computer instead of Raspberry Pi
- Add support for Google Drive instead of Dropbox
-   Use a Google sheet for questions instead of CSV so questions can be edited through a browser.



## Resources

[The Participatory Museum](http://www.participatorymuseum.org/)
