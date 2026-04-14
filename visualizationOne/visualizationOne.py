# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

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
#TODO this is actually in a very usuable form, maybe I should just save this to a csv and use it instead of og data?
dfVoteExtracted = pd.DataFrame(dataforVote)

#!CHANGE THE TITLE FOR THIS FIGURE
#TODO, change the mini-pop up key text, choose a better font
voteFig = px.line(dfVoteExtracted, x='Year', y=['White', 'Black', 'Asian', 'Hispanic (Any Race)'], title='Please God')
#voteFig.show()


rawIncomeDf = pd.read_csv('../data/racialIncome.csv')
rawIncomeDf = rawIncomeDf.drop(rawIncomeDf.columns[0:11], axis=1).reset_index(drop=True)
rawIncomeDf = rawIncomeDf.drop(rawIncomeDf.columns[1:4], axis=1).reset_index(drop=True)

incomeDf = pd.DataFrame(index=range(92), columns=['Median Income', 'Year', 'Race' ])
# set up year and race labels for the income dataframe
year = 2024
iteratorThruRaw = 0
for i in range(0, 92) :
    incomeDf.loc[i, 'Year'] = year
    year = year -1 if year > 2002 else  2024 
    if i < 23:
        incomeDf.loc[i, 'Race'] = 'White'
    elif i >= 23 and i < 46:
        incomeDf.loc[i, 'Race'] = 'Black'
    elif i >= 46 and i < 69:
        incomeDf.loc[i, 'Race'] = 'Asian'
    else:
        incomeDf.loc[i, 'Race'] = 'Hispanic (Any Race)'
        # find instances in og data frame relate to the specific race entries we desire. then start putting it in new dataframe
    while (rawIncomeDf.loc[iteratorThruRaw, 'Race'] != 'WHITE ALONE, NOT HISPANIC' and rawIncomeDf.loc[iteratorThruRaw, 'Race'] != 'BLACK ALONE'
           and rawIncomeDf.loc[iteratorThruRaw, 'Race'] != 'ASIAN ALONE' and rawIncomeDf.loc[iteratorThruRaw, 'Race'] !=  'HISPANIC (ANY RACE)'):
        #print((rawIncomeDf.loc[iteratorThruRaw, 'Race']))
        iteratorThruRaw += 1
    if rawIncomeDf.loc[iteratorThruRaw, 'Year'] == 2013:
        iteratorThruRaw += 1 #data has two entries for the year 2013 because of an additional census. the second entry has more addresses, so we use that one
    incomeDf.loc[i, 'Median Income'] = rawIncomeDf.loc[iteratorThruRaw, 'Median Estimate']
    iteratorThruRaw += 1 
    if rawIncomeDf.loc[iteratorThruRaw, 'Year'] == 2017 :
        iteratorThruRaw += 1 #data has two entries for the year 2017 due to updated processing system. Use the first, skip the second. same for 2013, only it is due to the 
    
print(incomeDf)
incomeDf.to_csv('test.csv')