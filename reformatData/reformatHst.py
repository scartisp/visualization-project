# Written by: Simion Cartis
import pandas as pd
import numpy as np

rawTable = pd.read_excel("../data/hst_vote01.xlsx", header=None)
rawTable = rawTable[7:38]

colsToDrop = rawTable.columns[2:13:2]
rawTable = rawTable.drop(columns=colsToDrop)

replaceNInCols = rawTable.columns[2:14]
rawTable[replaceNInCols] = rawTable[replaceNInCols].replace('N', np.nan)

rawTable = rawTable.rename(columns= {
    0: 'Year',
    1: 'Total Voting-Age Population',
    3: 'Total Percent',
    5: 'White',
    7: 'White Non-Hispanic',
    9:'Black',
    11: 'Asian',
    13: 'White Hispanic (Any Race)',
    14: 'Total Male Population Percentage',
    15: 'Total Female Population Percentage'
})

print(rawTable)