import pandas as pd

rawTable = pd.read_excel('../data/vote07_2024.xlsx', header= None)
rawTable = rawTable[7:17]
rawTable = rawTable.iloc[:, [1, 11, 13]]

tableReformated = rawTable.rename(columns= {
    1: 'Income Amount',
    11: 'Percent Reported Voted',
    13: 'Percent Reported Not voted'
})

print(tableReformated)
tableReformated.to_csv('../data/incomeVote.csv')