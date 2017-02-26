#!/usr/bin/python
import pandas as pd
import sqlite3

from bokeh.charts import Histogram, output_file, show
from bokeh.layouts import row

conn = sqlite3.connect('../srvy.db')
df = pd.read_sql_query('SELECT * FROM responses;',conn)


hist = Histogram(df, values = 'score', label = 'date' , agg = 'count', 
	title = 'Test Chart', legend = 'top_right', plot_width = 600) 

show(hist)
