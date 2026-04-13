# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

dfIncome = pd.read_excel('../data/tableA2.xlsx', header=None)
dfIncome = dfIncome.drop(dfIncome.index[0:66])
dfIncome = dfIncome.drop(dfIncome.index[425:518])
dfIncome = dfIncome.drop(columns=dfIncome.columns[2:12])
dfIncome = dfIncome.drop(columns=dfIncome.columns[4:6])
#print(dfIncome)


#make the line chart for the information about racial voting patterns
def removeInvalidVoteData(voteData):
    return [None if isinstance(x, str) else x for x in voteData]

#get rid of the information that is not relevant
dfVote = pd.read_excel('../data/hst_vote01.xlsx', header=None)
dfVote = dfVote.drop(dfVote.index[38:356])
dfVote = dfVote.drop(dfVote.index[0:4])
dfVote = dfVote.drop(columns=dfVote.columns[14:16])
dfVote = dfVote.drop(columns=dfVote.columns[2::2])

#this isn't done smartly, but whatever. Get the different parts, put them all into arrays which are then put into a dict
voteYears = voteWhiteNonHis = dfVote.iloc[3:27, 0].dropna().to_list()
voteWhite = dfVote.iloc[2:27, 3].dropna().to_list()
voteWhite = removeInvalidVoteData(voteWhite)

voteWhiteNonHis = dfVote.iloc[2:27, 4].dropna().to_list()
voteWhiteNonHis = removeInvalidVoteData(voteWhiteNonHis)

voteBlack = dfVote.iloc[2:27, 5].dropna().to_list()
voteBlack = removeInvalidVoteData(voteBlack)

voteAsian = dfVote.iloc[2:27, 6].dropna().to_list()
voteAsian = removeInvalidVoteData(voteAsian)


voteHispanic = dfVote.iloc[2:27, 7].dropna().to_list()
voteHispanic = removeInvalidVoteData(voteHispanic)


dataforVote = {
    'Year': voteYears,
    'White': voteWhite,
    'White Non-Hispanic': voteWhiteNonHis,
    'Black': voteBlack,
    'Asian': voteAsian,
    'Hispanic (Any Race)': voteHispanic    
}

#make data frame from dict
dfVoteExtracted = pd.DataFrame(dataforVote)

#!CHANGE THE TITLE FOR THIS FIGURE
voteFig = px.line(dfVoteExtracted, x='Year', y=['White', 'White Non-Hispanic', 'Black', 'Asian', 'Hispanic (Any Race)'], title='Please God')
voteFig.show()

