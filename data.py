"""
This is a simple graph to show the frequency of a college that NBA players went to before getting drafted.
CSV file by Justinas Cirtautas
Link to CSV: https://www.kaggle.com/justinas/nba-players-data
"""
import pandas as pd
import plotly.express as px
data = pd.read_csv('all_seasons.csv')
df1 = data.groupby(['college']).count().reset_index()
df2 = df1.head(25)
fig1 = px.bar(
        df2,
        y=data.groupby(['college']).size(),
        x='college',
        color='college')
fig1.show()
