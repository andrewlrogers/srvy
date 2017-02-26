#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string

from bokeh.charts import Bar, Scatter,  output_file, show

#Get time in order
today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
fixed_date = '2017-02-19'

#getting yesterday variable into the sqlite3 query. If you know a better way please use it.
yesterday_query = "SELECT * FROM responses WHERE date = '?';"
yesterday_query= string.replace(yesterday_query, '?', fixed_date)

#test query to see all output.
all_query = "SELECT * FROM responses"

#set-up our sql cursor
conn = sqlite3.connect('../srvy.db')

#Setting up our data frame
df = pd.read_sql_query(yesterday_query, conn, parse_dates= 'time')
by_question = df.groupby('question')

#The actual chart
bar = Bar(df, values = 'score', label = 'question', stack =  'score',
     title = 'Test Chart for ' + yesterday, agg = 'count', legend= 'bottom_left', plot_height = 900, plot_width = 900)

scatter = Scatter(df, x = 'time', y ='date' )


#We can change path.
output_file('../export/hist.html')

#we wont need to show the final chart, but good for testing
show(bar)
