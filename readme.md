# SRVY
## A Physical Like/Dislike Questionnaire for Non-Profits
===
---

## Overview / Functionality
SRVY uses a screen to pose a visitor a question and then records their response using two physical buttons that correspond to two different values (Like, Dislike). The response is recorded in a SQLite3 database. On a daily basis SRVY generates a series of charts and reports which are automatically uploaded to a Dropbox application. Questions can be appended on a daily basis by editing a .CSV file also located in the Dropbox account.

The intended audience is smaller art non-profits such as museums, theaters, and community art centers. The goal is to provide a low-cost and customizable tool that will allow organizations to track audience engagement and determine metrics of success with little daily upkeep.

- 2:00AM (No one should be responding to a questionnaire this late)
-  Stop collecting responses.
-  **Chart**
-   Previous day's responses charted into digest.
-   Previous day's responses converted into csv
-  **Synch**
-   Digest and csv uploaded to Dropbox.
-   .csv and .db files overwritten on Dropbox.
-   questions.csv downloaded from Dropbox.
-  Reboot
-  Begin collecting responses.


- **SRVY**
-   Top level directory with main functionality
- **Export**
-   Contains charts and csv's that are backed-up on Dropbox
- **Synch**
-   Generates charts and csv's that are stored in **Export**
-   Contains script to pull questions from Dropbox


## Requirements
### Hardware
### Packages

## Installation

### Dropbox
1. Create a file named dropbox.config and save it to the home directory of srvy
2. Add the following lines to dropbox.config:

```
#!config

[dropbox]
token = "INSERT YOUR PRIVATE DROPBOX TOKEN HERE"
```

and paste your private Dropbox token between the quotes.

### Customization

### Possible Future Functionality

- Add support for C.H.I.P computer instead of Raspberry Pi
- Add support for Google Drive instead of Dropbox
-   Use a Google sheet for questions instead of CSV so questions can be edited through a browser.



## Resources

[The Participatory Museum](http://www.participatorymuseum.org/)