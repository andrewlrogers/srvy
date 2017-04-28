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
### Config file
1. Find the file **srvy.config.example**. Rename it **srvy.config**.

### Dropbox
1. Open **srvy.config** in a text editor.
2. Find the the [dropbox] section:

  ```
  #!config

  [dropbox]
  token = INSERT_YOUR_PRIVATE_DROPBOX_TOKEN_HERE
  ```

3. Replace INSERT_YOUR_PRIVATE_DROPBOX_TOKEN_HERE with your private Dropbox token.
4. Save **srvy.config**

### Customization

### Possible Future Functionality

- Add support for C.H.I.P computer instead of Raspberry Pi
- Add support for Google Drive instead of Dropbox
-   Use a Google sheet for questions instead of CSV so questions can be edited through a browser.



## Resources

[The Participatory Museum](http://www.participatorymuseum.org/)
