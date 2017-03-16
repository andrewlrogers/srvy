#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show
from bokeh.layouts import row

"""time variables"""
fixed_date = '2017-02-26'
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
database_file = "../srvy.db"

def get_unique_questions(df):
    """Creates a list of all unique questions from a given date"""
    questions=[]
    for question in df['question']:
        if question not in questions:
            questions.append(question)
    return(questions)

def load_dataframe(date):
    conn = sqlite3.connect(database_file)
    sql_query = "SELECT * FROM responses where date ='" + str(date) + "'"
    df = pd.read_sql_query(sql_query, conn)
    return(df)

def create_charts_for_all_questions(date):
    """Creates charts for all unique questions from a given date"""
    df= load_dataframe(date)
    questions = get_unique_questions(df)
    chart_group = []
    for q in questions:
        individual_question_bar = Bar(df.loc[df['question'] == q].sort_values(by='score', ascending = False), values = 'score', label = 'question', stack = 'opinion', title = q + ' ' + yesterday, ylabel = 'Number of Responses', xlabel=' ', agg = 'count', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',])
        chart_group.append(individual_question_bar)

    all_questions = Bar(df, values = 'score', label = 'question', stack = 'opinion', title= 'All questions ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend = 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',])
    chart_group.append(all_questions)

    donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)
    chart_group.append(donut_chart)
    output_file('../export/'+ date + '_digest.html')
    show(row(chart_group))

#The actual chart
#donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)
#chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')

create_charts_for_all_questions(fixed_date)
