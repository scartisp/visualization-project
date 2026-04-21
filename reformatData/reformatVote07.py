#written by: Simion Cartis
import pandas as pd

rawTable = pd.read_excel('../data/vote07_2024.xlsx', header= None)
rawTable = rawTable[7:17]
rawTable = rawTable.iloc[:, [1, 10, 11, 12, 13]]

tableReformated = rawTable.rename(columns= {
    1: 'Income Amount',
    11: 'Percent Reported Voted',
    10: 'Amount Reported Voted',
    12: 'Amount Reported Not Voted',
    13: 'Percent Reported Not voted'
})
tableReformated['Income Amount'] = tableReformated['Income Amount'].replace({
    'Under $10,000' : 'Under 10,000',
    '$10,000 to $14,999': "10k-19k",
    '$15,000 to $19,999': '15k-19k',
    '$20,000 to $29,999': '20k-29k',
    '$30,000 to $39,999': '30k-39k',
    '$40,000 to $49,999': '40k-49k',
    '$50,000 to $74,999': '50k-74k',
    '$75,000 to $99,999': '75k-99k',
    '$100,000 to $149,999': '100k-149k',
    '$150,000 and over': '150,000 and over'
})

print(tableReformated)
tableReformated.to_csv('../data/incomeVote.csv')