# Written by: Simion Cartis

import pandas as pd
import plotly.express as px

#data frame for the vote data
voteDf = pd.read_csv('../data/racialVote.csv')

voteDf = voteDf.drop(voteDf.columns[[0,2,3,4,9,10]], axis=1)
#melt changes format. id_vars= 'Year' keeps the year column the same. 'var_name='Race' creates a new column out of the previous column titles (minus Year Col)
#'value_name' creates a new column out of the pieces of data that are in the original columns
voteDf = voteDf.melt(id_vars='Year', var_name='Race', value_name='Voting Percentage')
#voteDf.to_csv('test.csv')
#print(voteDf)


rawIncomeDf = pd.read_csv('../data/racialIncome.csv')
rawIncomeDf = rawIncomeDf.drop(rawIncomeDf.columns[0:11], axis=1).reset_index(drop=True)
rawIncomeDf = rawIncomeDf.drop(rawIncomeDf.columns[1:4], axis=1).reset_index(drop=True)

#data frame for the income data
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

#incomeDf.to_csv('test.csv')

#do an inner combination on incomeDf (since it has fewer years)
#get the race, year, and voting percentage columns from voteDf, inner merge on race and year (although they share the same race info)
combinedDf = incomeDf.merge(voteDf[['Race', 'Year', 'Voting Percentage']],
                             on=['Race', 'Year'], how='inner')

#combinedDf.to_csv('combined.csv')

yearList = list(range(2002, 2025, 1))  # 2024 down to 2002

scatterFig = px.scatter(
    combinedDf,
    x="Voting Percentage",
    y="Median Income",
    color="Race",
    animation_frame="Year",
    category_orders={"Year": yearList},
    custom_data=['Race'],
    title="Median Income vs Voting Percentage by Race",
    color_discrete_sequence= px.colors.qualitative.G10
)
scatterFig.update_xaxes(range=[20, 80])  
scatterFig.update_yaxes(range=[30000, 130000])
scatterFig.update_traces(
    marker=dict(size=20),
    hovertemplate= 'Race: %{customdata[0]}<br>' + 'Voting Percentage: %{x}%<br>' + 'Median Income: %{y}<extra></extra>'
)
scatterFig.update_layout(
    plot_bgcolor='black',
    font_family='balto',
    title_font_size=30,
    sliders=[{
        'currentvalue': {'prefix': 'Year: '}
    }]
)
scatterFig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1200
scatterFig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 400
# scatterFig.show()
#scatterFig.write_html('scatterPlot.html', auto_play=False)

#scatter plots for primary years
primaryDf = combinedDf[combinedDf['Year'] % 4 == 0]
primaryYears = list(range(2004, 2025, 4)) 
primaryFig = px.scatter(
    primaryDf,
    x="Voting Percentage",
    y="Median Income",
    color="Race",
    animation_frame="Year",
    category_orders={"Year": primaryYears},
    custom_data=['Race'],
    title="Median Income vs Voting Percentage by Race for Primary Years",
    color_discrete_sequence= px.colors.qualitative.G10
)
primaryFig.update_xaxes(range=[40, 80])  
primaryFig.update_yaxes(range=[30000, 130000])
primaryFig.update_traces(
    marker=dict(size=20),
    hovertemplate= 'Race: %{customdata[0]}<br>' + 'Voting Percentage: %{x}%<br>' + 'Median Income: %{y}<extra></extra>'
)
primaryFig.update_layout(
    plot_bgcolor='black',
    font_family='balto',
    title_font_size=30,
    sliders=[{
        'currentvalue': {'prefix': 'Year: '}
    }]
)
primaryFig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1200
primaryFig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 400

#primaryFig.show()

midtermDf = combinedDf[combinedDf['Year'] % 4 != 0]
midtermYears = list(range(2002, 2022, 4)) 
midtermFig = px.scatter(
    midtermDf,
    x="Voting Percentage",
    y="Median Income",
    color="Race",
    animation_frame="Year",
    category_orders={"Year": midtermYears},
    custom_data=['Race'],
    title="Median Income vs Voting Percentage by Race for Midterm Years",
    color_discrete_sequence= px.colors.qualitative.G10
)
midtermFig.update_xaxes(range=[20, 60])  
midtermFig.update_yaxes(range=[30000, 130000])
midtermFig.update_traces(
    marker=dict(size=20),
    hovertemplate= 'Race: %{customdata[0]}<br>' + 'Voting Percentage: %{x}%<br>' + 'Median Income: %{y}<extra></extra>'
)
midtermFig.update_layout(
    plot_bgcolor='black',
    font_family='balto',
    title_font_size=30,
    sliders=[{
        'currentvalue': {'prefix': 'Year: '}
    }]
)
midtermFig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1200
midtermFig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 400

#midtermFig.show()