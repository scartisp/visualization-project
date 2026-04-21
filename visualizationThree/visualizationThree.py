# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

def changeFig(fig):
    fig.update_layout(
        plot_bgcolor='black',
        font_family='balto',
        title_font_size=30
    )


incomeVoteDf = pd.read_csv('../data/incomeVote.csv')
incomeVoteDf = incomeVoteDf[['Income Amount', 'Percent Reported Voted']]

incomeVoteFig = px.histogram(incomeVoteDf, x='Income Amount', y='Percent Reported Voted', title= 'Percent Reported Voted by Income Range', color_discrete_sequence= px.colors.qualitative.G10)
incomeVoteFig.update_layout(bargap=0.001)
incomeVoteFig.update_yaxes(title='Percent Reported Voted')
incomeVoteFig.update_xaxes(title='Income Amount in USD')
incomeVoteFig.update_layout(
        font_family='balto',
        title_font_size=30
    )
incomeVoteFig.update_traces(
    hovertemplate= 'Income Amount: %{x}<br>' + 'Percent Reported voted: %{y}%<extra></extra>'
)
incomeVoteFig.show()

