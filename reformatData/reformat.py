#Written by: Simion Cartis
import pandas as pd

rawtableA2 = pd.read_excel("../data/tableA2.xlsx", header=None)

# Find the first row that is the footer's. footer_idx is a pandas.Index object
footer_idx = rawtableA2.index[rawtableA2[0].astype(str).str.match(r"^N Not available\.", na=False)]
footer_start = footer_idx[0] if len(footer_idx) else len(rawtableA2) # if footer found, mark it's index. If not, just use the whole data frame
bodyTableA2 = rawtableA2.iloc[5:footer_start].copy()
#get four digit numbers for the rear column
bodyTableA2["Year"] = bodyTableA2[0].astype(str).str.extract(r"^\s*(\d{4})")[0].astype("Int64")
#the ones that aren't years are races
bodyTableA2["Race"] = bodyTableA2[0].where(bodyTableA2["Year"].isna()).ffill()

dfTableA2 = bodyTableA2[bodyTableA2["Year"].notna()].copy()

#get rid of the first column as we extracted its data and put them into the Year and Race columns
dfTableA2 = dfTableA2.drop(columns=[0]).reset_index(drop=True)
dfTableA2 = dfTableA2.rename(columns= {
    1: 'Number (thousands)',
    2: 'Total',
    3: 'Under $15,000',
    4:'$15,000 to $24,999',
    5: '$25,000 to 34,999',
    6: '$35,000 to 49,999',
    7: '$50,000 to 74,999',
    8: '$75,000 to $99,999',
    9: '$100,000 to 149,999',
    10: '$150,000 to $199,999',
    11: '$200,000 and over',
    12: 'Median Estimate',
    13: 'Median margin of error^2 (+/-)',
    14: 'Mean Estimate',
    15: 'Mean margin of error^2 (+/-)'
})

#dfTableA2.to_csv('../data/racialIncome.csv')
print(dfTableA2)