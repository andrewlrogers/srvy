import sqlite3
from sqlite3 import Error

def create_conection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def create_table(db_file,create_table_sql):
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
    finally:
        conn.close

def main():
    database = "../archive/srvy.db"
    create_conection(database)
    create_srvy_table = """ CREATE TABLE IF NOT EXISTS responses (response_key INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    pythonDateTime TEXT NOT NULL,
                    unixTime REAL NOT NULL,
                    question TEXT NOT NULL,
                    opinion INTEGER NOT NULL
                    );"""
    create_table(database, create_srvy_table)

main()
