#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string
import os.path
import time

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show
from bokeh.layouts import row, column, gridplot

""" G L O B A L """
""" V A R I A B L E S """

database_file = "../srvy.db"

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
now_datetime = time.mktime((datetime.now()).timetuple()) #returns the dateime as a timestamp
prev_datetime = time.mktime((datetime.now() - timedelta(days=10)).timetuple())

## SQLITE3 VARIABLES
sql_query = 'SELECT * FROM responses WHERE unixTime BETWEEN ' + str(prev_datetime) + ' AND ' + str(now_datetime) + ' '
conn = sqlite3.connect(database_file)

""" F U N C T I O N S """
def create_output_directory(date):
    """Creates output directory for charts, using date for organization"""
    directory = '../export/' + str(date) + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_unique_questions(df):
    """Creates a list of all unique questions from dataframe query"""
    questions=[]
    for question in df['question']:
        if question not in questions:
            questions.append(question)
    return(questions)

def generate_dataframe():
    """From create_all_charts reurns value for df"""
    df = pd.read_sql_query(sql_query, conn, parse_dates=['pythonDateTime'])
    return(df)


""" M A I N """
""" F U N C T I O N """

def create_all_charts():
    """Creates charts for all unique questions from a given date"""
    df = generate_dataframe()
    questions = get_unique_questions(df)
    chart_group = []

    #CHARTS FOR EACH INDIVIDUAL QUESTION
#    for question in questions:
#        print("Creating chart for question: " + str(question))
#        bar = Bar(df.loc[df['question'] == question].sort_values(by='opinion', ascending = False), values = 'opinion', label = 'question', stack = 'opinion', title = question + ' ' + yesterday, ylabel = 'Number of Responses', agg = 'mean', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',])
#        chart_group.append(bar)

#    for question in questions:
#        print("Creating timeline for question: " + str(question))
#        time_line = TimeSeries(df.loc[df['question'] == question], x = 'time', y = 'question', builder_type = 'point', color = 'score', marker = 'score')
#        chart_group.append(time_line)

    #STAND ALONE CHARTS
    donut_chart = Donut(df, label='opinion', values = 'opinion' )

    bar_chart= Bar(df.loc[df['question'] == 'Did you enjoy your visit?'], values = 'opinion', label = 'pythonDateTime', stack='opinion', agg = 'sum')
#    time_line = TimeSeries(df, x = 'time', y = 'question', builder_type = 'point', color = 'score', marker = 'score')

    output_file('../export/' + str(today) + '.html') # Creates single .html file with all charts

    show(bar_chart)
    #set layout and show digest chart
    #grid = gridplot(chart_group, ncols=3, plot_width = 400)
    #show(column( donut_chart ,grid))
    #show(column(grid))


#create_output_directory(today)
create_all_charts()
