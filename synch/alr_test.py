#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string
import os.path

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show
from bokeh.layouts import row

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
    sql_query = c.execute("SELECT DISTINCT question FROM responses where date ='" + str(date) + "'")

    for question in sql_query:
        questions.append(question)

    return(questions)

def query_by_question(question):
    """Queries the database from a question string"""
    sql_query = "SELECT * FROM responses where question ='" + str(question) + "'"
    return(sql_query)

def create_output_directory(date):
    """Creates output directory for charts, using date for organization"""
    directory = '../export/' + str(date) + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_charts_for_all_questions(date):
    """Creates charts for all unique questions from a given date"""
    conn = sqlite3.connect(database_file)
    sql_query = query_by_date(date)
    questions = get_unique_questions(date)
    chart_group = []
    count = 1

    create_output_directory(date)
    df = pd.read_sql_query(sql_query, conn)
    for question in questions:
        print("Creating chart for question: " + str(question[0]))

        bar = Bar(df.loc[df['question'] == question[0]].sort_values(by='score', ascending = False), values = 'score', label = 'question', stack = 'opinion', title = question[0] + ' ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',] ,plot_height = 900, plot_width = 600)

        #by_question = df.groupby('question').size()
        #bar1 = Bar(df.sort_values(by='score', ascending = True), values = 'score', label = 'question', stack =  'opinion', title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'] ,plot_height = 900, plot_width = 900)

        chart_group.append(bar)
        count += 1

    # Create single .html file with all charts
    output_file('../export/' + str(date) + '/' + 'all_questions_' + str(date) + '.html')
    show(row(chart_group))



#The actual chart
#donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)
#chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')

create_charts_for_all_questions('2017-02-26')
