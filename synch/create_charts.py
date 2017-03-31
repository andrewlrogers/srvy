#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string
import os.path

from bokeh.charts import Bar, Donut, TimeSeries, Line, output_file, show
from bokeh.layouts import row, column, gridplot

""" G L O B A L """
""" V A R I A B L E S """

database_file = "../srvy.db"
#Get time in order
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

""" F U N C T I O N S """

def query_by_date(date): #Queries the database from a date string in the format YYYY-MM-DD
    sql_query = "SELECT * FROM responses where date ='" + str(date) + "'"
    return(sql_query)

def get_unique_questions(df): #Creates a list of all unique questions from dataframe query
    questions=[]
    for question in df['question']:
        if question not in questions:
            questions.append(question)
    return(questions)

def create_output_directory(date): #Creates output directory for charts, using date for organization
    directory = '../export/' + str(date) + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

#def query_by_question(question): #Queries the database from a question string
#    sql_query = "SELECT * FROM responses where question ='" + str(question) + "'"
#    return(sql_query)

def generate_dataframe(date): #From create_charts_for_all_questions reurns value for df
        conn = sqlite3.connect(database_file)
        sql_query = query_by_date(date)
        pd.read_sql_query(sql_query, conn)
        return(pd.read_sql_query(sql_query, conn))


""" M A I N """
""" F U N C T I O N """

def create_charts_for_all_questions(date): #Creates charts for all unique questions from a given date
    df = generate_dataframe(date)
    chart_group = []
    questions = get_unique_questions(df)

    #CHARTS FOR EACH INDIVIDUAL QUESTION
    for question in questions:
        print("Creating chart for question: " + str(question))
        bar = Bar(df.loc[df['question'] == question].sort_values(by='score', ascending = False), values = 'score', label = 'question', stack = 'opinion', title = question + ' ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',])
        chart_group.append(bar)

    for question in questions:
        print("Creating timeline for question: " + str(question))
        time_line = TimeSeries(df.loc[df['question'] == question], x = 'time', y = 'question', builder_type = 'point', color = 'opinion', marker = 'opinion')
        chart_group.append(time_line)

    #STAND ALONE CHARTS
    donut_chart= Donut(df, values = 'score', label = ['opinion', 'question'], title = 'Opinon distibution from ' + date, ylabel = 'Number of Responses', agg = 'count', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',], width= 800, height = 850)
    time_line = TimeSeries(df, x = 'time', y = 'question', builder_type = 'point', color = 'opinion', marker = 'opinion')

    output_file('../export/' + str(date) + '.html') # Creates single .html file with all charts

    #set layout and show digest chart
    grid = gridplot(chart_group, ncols=3, plot_width = 400)
    #show(column( time_line, donut_chart ,grid))
    show(column(grid))



create_charts_for_all_questions('2017-02-26')
