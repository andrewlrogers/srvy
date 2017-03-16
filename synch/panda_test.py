#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show
from bokeh.layouts import row

"""time variables"""
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

"""initialize variables"""


"""Create df from SQL"""

database_file = "../srvy.db"
conn = sqlite3.connect(database_file)
sql_query = "SELECT * FROM responses where date ='" + str('2017-02-26') + "'"
df = pd.read_sql_query(sql_query, conn)


def get_unique_questions():
    """Creates a list of all unique questions from a given date"""
    questions=[]
    for question in df['question']:
        if question not in questions:
            questions.append(question)
    return(questions)


def create_charts_for_all_questions():
    """Creates charts for all unique questions from a given date"""
    questions = get_unique_questions()
    chart_group = []
    count = 1
    for q in questions:
        bar = Bar(df.loc[df['question'] == q].sort_values(by='score', ascending = False), values = 'score', label = 'question', stack = 'opinion', title = q + ' ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc',] ,plot_height = 900, plot_width = 600)
        output_file('../export/question' + str(count) + '.html')
        count += 1
        #show(bar)
        chart_group.append(bar)
    show(row(chart_group))

#The actual chart
#donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)
#chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')

create_charts_for_all_questions()
