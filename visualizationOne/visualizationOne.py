# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

voteDf = pd.read_csv('../data/racialVote.csv')

voteDf = voteDf.drop(voteDf.columns[[0,2,3,4,9,10]], axis=1)
#melt changes format. id_vars= 'Year' keeps the year column the same. 'var_name='Race' creates a new column out of the previous column titles (minus Year Col)
#'value_name' creates a new column out of the pieces of data that are in the original columns
voteDf = voteDf.melt(id_vars='Year', var_name='Race', value_name='Voting Percentage')
voteDf.to_csv('test.csv')
#print(voteDf)

voteFig = px.line(voteDf, x='Year', y='Voting Percentage', color='Race', title='Change in Voting Percentage Over Time' )
#start earlier (because NaN values make the og range too large)
voteFig.update_xaxes(range= [1978, 2024])
#update color of background
voteFig.update_layout(
    plot_bgcolor='black'
)
# voteFig.show()


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
        incomeDf.loc[i, 'Race'] = 'White Non-Hispanic'
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

incomeFig = px.line(incomeDf, x='Year', y='Median Income', color='Race', title= "Change in Median Income Over Time")
incomeFig.update_layout(
    plot_bgcolor='black'
)
#incomeFig.show()
#TODO Make titles bigger, choose better color scheme, choose better font? add dots to data points?
with open('lineCharts.html', 'w') as f:
    f.write(voteFig.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(incomeFig.to_html(full_html=False, include_plotlyjs=False))
    
#print(incomeDf)
#incomeDf.to_csv('test.csv')