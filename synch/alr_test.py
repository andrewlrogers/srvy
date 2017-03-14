#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string

from bokeh.charts import Bar, Donut, TimeSeries, output_file, show

#Get time in order
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
fixed_date = '2017-02-26'

#getting yesterday variable into the sqlite3 query. If you know a better way please use it.
yesterday_query = "SELECT * FROM responses WHERE date = '?';"
yesterday_query= string.replace(yesterday_query, '?', fixed_date)

#test query to see all output.
all_query = "SELECT * FROM responses"

#set-up our sql cursor
conn = sqlite3.connect('../srvy.db')

#Setting up our data frame
df = pd.read_sql_query(all_query, conn, parse_dates= 'time')
by_question = df.groupby('question').size()

#The actual chart
bar1 = Bar(df, values = 'score', label = 'question', stack =  'opinion', title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count', legend= 'bottom_left', palette= ['#084594', '#2171b5', '#4292c6', '#6baed6', '#9ecae1', '#c6dbef', '#deebf7', '#f7fbff'] ,plot_height = 900, plot_width = 900)

donut_chart= Donut(df, values = 'score', label = ['opinion'], title = 'Opinon distibution from ' + yesterday, ylabel = 'Number of Responses', agg = 'count',)

chron_chart = TimeSeries(df,x = 'time', y = 'opinion', color= 'question', dash='question')
#We can change path.
output_file('../export/hist.html')


#we wont need to show the final chart, but good for testing
show(bar1)
