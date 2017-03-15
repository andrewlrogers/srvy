#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show

database_file = "../srvy.db"

#Get time in order
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

def query_by_date(date):
    """Queries the database from a date string in the format YYYY-MM-DD"""
    sql_query = "SELECT * FROM responses where date ='" + str(date) + "'"
    return(sql_query)

def get_unique_questions(date):
    """Creates a list of all unique questions from a given date"""
    questions = []
    conn = sqlite3.connect(database_file)
    c = conn.cursor()
    sql_query = c.execute(query_by_date(date))

    for response in sql_query:
        if response[3] not in questions:
            questions.append(response[3])
    print(questions)
    return(questions)

get_unique_questions('2017-02-26')
#test query to see all output.
sql_query = query_by_date('2017-02-26')

#set-up our sql cursor
conn = sqlite3.connect(database_file)

#Setting up our data frame
# parse_dates='time' gives a KeyError
df = pd.read_sql_query(sql_query, conn)
by_question = df.groupby('question').size()

#The actual chart
bar1 = Bar(df, values = 'score', label = 'question', stack =  'opinion', title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'] ,plot_height = 900, plot_width = 900)

donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)

chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')
#We can change path.
output_file('../export/hist.html')


#we wont need to show the final chart, but good for testing
show(bar1)
