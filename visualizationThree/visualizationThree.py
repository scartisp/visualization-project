# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

def changeFig(fig):
    fig.update_layout(
        font_family='balto',
        title_font_size=30
    )


incomeVoteDf = pd.read_csv('../data/incomeVote.csv')
incomeVoteDf = incomeVoteDf[['Income Amount', 'Percent Reported Voted']]

incomeVoteFig = px.histogram(incomeVoteDf, x='Income Amount', y='Percent Reported Voted', title= 'Percent Reported Voted by Income Range, 2024', color_discrete_sequence= px.colors.qualitative.G10)
incomeVoteFig.update_layout(bargap=0.001)
incomeVoteFig.update_yaxes(title='Percent Voted')
incomeVoteFig.update_xaxes(title='Income Amount in USD')
changeFig(incomeVoteFig)
incomeVoteFig.update_traces(
    hovertemplate= 'Income Amount: %{x}<br>' + 'Percent voted: %{y}%<extra></extra>'
)
incomeVoteFig.show()

raceVoteDf = pd.read_csv('../data/racialVote.csv')

raceVoteDf = raceVoteDf.drop(raceVoteDf.columns[[0,2,3,4,9,10]], axis=1)
raceVoteDf = raceVoteDf.head(1)
#since the income vote data is only for the year 2024, we only want info from 2024
raceVoteDf = raceVoteDf.melt(id_vars='Year', var_name='Race', value_name='Voting Percentage')
raceVoteDf = raceVoteDf[['Race', 'Voting Percentage']]
raceVoteFig = px.bar(raceVoteDf, x='Race', y='Voting Percentage', color='Race', title='Voting Percentage by Race, 2024', color_discrete_sequence= px.colors.qualitative.G10)
changeFig(raceVoteFig)
raceVoteFig.update_traces(
    hovertemplate= 'Race: %{x}<br>' + 'Percent voted: %{y}%<extra></extra>'
)
#! I don't really know if I like this bar chart, feels a little needless. Might want to scrap and just replace with layered histogram
#! maybe I do like it, idk
raceVoteFig.show()