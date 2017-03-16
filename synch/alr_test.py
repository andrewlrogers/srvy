#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string
import os.path

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show
from bokeh.layouts import row, column, gridplot

database_file = "../srvy.db"

#Get time in order
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

def query_by_date(date):
    """Queries the database from a date string in the format YYYY-MM-DD"""
    sql_query = "SELECT * FROM responses where date ='" + str(date) + "'"
    return(sql_query)

def get_unique_questions(df):
    """Creates a list of all unique questions from dataframe query"""
    questions=[]
    for question in df['question']:
        if question not in questions:
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
    df = pd.read_sql_query(sql_query, conn)
    questions = get_unique_questions(df)

    chart_group = []
    count = 1

    for question in questions:
        print("Creating chart for question: " + str(question))

        bar = Bar(df.loc[df['question'] == question].sort_values(by='score', ascending = False), values = 'score', label = 'question', stack = 'opinion', title = question + ' ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',])

        #by_question = df.groupby('question').size()
        #bar1 = Bar(df.sort_values(by='score', ascending = True), values = 'score', label = 'question', stack =  'opinion', title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'] ,plot_height = 900, plot_width = 900)

        chart_group.append(bar)
        count += 1

    donut_chart= Donut(df, values = 'score', label = ['opinion', 'question'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',], width= 800, height = 850)

    # Create single .html file with all charts
    output_file('../export/' + str(date) + '.html')

    #set layout and show digest chart
    grid = gridplot(chart_group, ncols=3, plot_width = 400)
    show(column(donut_chart,grid))



#The actual chart
#donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)
#chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')

create_charts_for_all_questions('2017-02-26')
