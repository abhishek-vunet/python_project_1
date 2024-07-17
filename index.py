import pandas as pd

#read the csv
df = pd.read_csv('data.csv')

#make a copy of dataframe
df2 = df

#add a column profit subtracting 2 columns
df2['Profit'] = df2['Sell Price'] - df2["Cost Price"]

#finding items with negative profit
temp = df2.loc[(df2['Profit'] < 0)]['Item Name']

#finding the total profit
totalProfit = df['Profit'].sum()

#Adding a new row for totalProfit
df3 = {'Item Name':"Total Profit", "Profit":totalProfit}

#appending the row
df_final = df2._append(df3,ignore_index=True)

#make a new csv
df_final.to_csv("answer.csv")

#printing those with a loss
print("Items with loss are:")
for item in temp:
    print(item)