#!/usr/bin/python
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import string
import os.path
import time

from bokeh.charts import Bar, Donut, Line, output_file, show
from bokeh.layouts import row, column, gridplot

""" G L O B A L """
""" V A R I A B L E S """

database_file = "../srvy.db"

today = str(datetime.now().strftime('%Y-%m-%d'))
yesterday = str((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
now_datetime = time.mktime((datetime.now()).timetuple())  # returns the dateime as a timestamp
prev_datetime = time.mktime((datetime.now() - timedelta(days=10)).timetuple())

crocker_purple = ['#693A77', '#8b5c8e', '#ae7ea5', '#d1a1bc']
crocker_contrast = ['#693A77', '#A2AD00', '#565A5C']

## SQLITE3 VARIABLES
sql_query = 'SELECT * FROM responses WHERE unixTime BETWEEN ' + str(prev_datetime) + ' AND ' + str(now_datetime) + ' '
all_query = 'SELECT * FROM responses'
conn = sqlite3.connect(database_file)

""" F U N C T I O N S """


def create_output_directory(date):
    """Creates output directory for charts, using date for organization"""
    directory = '../export/' + str(date) + '/'
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_unique_questions(df):
    """Creates a list of all unique questions from dataframe query"""
    questions = []
    for question in df['question']:
        if question not in questions:
            questions.append(question)
    return (questions)


def generate_dataframe():
    """From create_all_charts reurns value for df"""
    df = pd.read_sql_query(all_query, conn, parse_dates=['pythonDateTime'])
    df['hour'] = df['pythonDateTime'].dt.strftime('%H')  # Adds hour Column with hour as 24 hour padded
    df['dayweek'] = df['pythonDateTime'].dt.strftime('%A')  # Adds dayweek Column with Monday, Tuesday, etc style
    df['month'] = df['pythonDateTime'].dt.strftime('%b')  # Adds month column with Sep, Oct, Nov style formatting
    df['like_dislike'] = df['opinion']  # duplicates opinion column as like_dislike
    df.ix[
        df.opinion > 0, 'like_dislike'] = 'Liked'  # if the value in opinion is > 0 then the value in like_dislike is 'Liked'
    df.ix[df.opinion < 0, 'like_dislike'] = 'Disliked'  # does the opposite as above
    return (df)


def create_scorecard(df):
    """"creates a dataframe that sums the opinion for each question"""
    questions = get_unique_questions(df)
    score = []
    question = []
    for q in questions:
        qs = df.loc[df['question'] == q, 'opinion'].sum()
        score.append(qs)
        question.append(q)
    data = {'question': question, 'score': score}
    df_score = pd.DataFrame(data, columns=['question', 'score'])
    return (df_score)


""" M A I N """
""" F U N C T I O N """

df = generate_dataframe()
df_score = create_scorecard(df)
chart_group = []
pie_group = []


def create_questions_chart():
    print('Creating bar chart for questions')  #
    question_bar = Bar(df.sort_values(by='opinion', ascending=False), title='Opinion reponses by question asked.',
                       values='like_dislike', label='question', stack='like_dislike', ylabel='Number of Responses',
                       agg='count', legend='top_right', palette=crocker_contrast)
    chart_group.append(question_bar)


def create_overall_likes_chart():
    print('Creating donut chart of overall like/dislike')
    donut_chart = Donut(df, title='Like and Dislike distribution', label=['like_dislike'], values='opinion',
                        agg='count', palette=crocker_purple)
    pie_group.append(donut_chart)


def create_hourly_bar_chart():
    print('Creating an hourly Bar Chart')
    hourly_bar = Bar(df.sort_values(by='opinion', ascending=False), title='Opinion by hour of the day',
                     values='opinion', label='hour', stack='like_dislike', xlabel='Hour of the Day',
                     ylabel='Number of Responses', agg='count', legend='top_right', palette=crocker_contrast)
    chart_group.append(hourly_bar)


def create_question_distribution_chart():
    print('Creating donut chart of question distribution')
    q_dist = Donut(df, title='Distribition of questions asked', label='question', hover_text='question',
                   hover_tool=True, values='question', agg='count', palette=crocker_purple)
    pie_group.append(q_dist)


def create_score_chart():
    print('Creating score')
    total_score = Bar(df_score, title='Score by question: 0 is neutral', label='question', values='score', legend=False,
                      ylabel='Score', palette=crocker_contrast)
    chart_group.append(total_score)


def create_output_file():
    output_file('../export/' + str(today) + '.html')  # Creates single .html file with all charts

    # show(time_line)
    # set layout and show digest chart
    pie_grid = gridplot(pie_group, ncols=2, plot_width=300, plot_height=300)
    chart_grid = gridplot(chart_group, ncols=1, plot_width=600)
    show(column(pie_grid, chart_grid))


def create_all_charts():
    """Creates charts for all unique questions from a given date"""
    create_questions_chart()
    create_overall_likes_chart()
    create_hourly_bar_chart()
    create_question_distribution_chart()
    create_score_chart()
    create_output_file()


create_all_charts()
