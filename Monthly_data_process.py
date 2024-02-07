# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:17:48 2024

@author: Safin.Lin
"""
import pandas as pd
import numpy as np


# Import the data
data = pd.read_csv('86027_csv.csv')
# Look at the data
data.head()

# Combine the date
data['date'] = pd.to_datetime(data[['Year', 'Month', 'Day']])
data.head()
data = data.set_index('date')
data.head()

# Delete Year, Month, and Day column
data = data.drop(['Year', 'Month', 'Day'], axis = 1)
data.head()


# Group monthly data
pivot_table = pd.pivot_table(data, index = data.index.month, columns = data.index.year, values = 'Rainfall (mm)', aggfunc=np.sum)

# Check column names
month = []
year = []

for i in range(1, pivot_table.shape[0] + 1):
    month.append(i)

for col in pivot_table:
    year.append(col)

rainfall_column = []
for i in range(len(year)):
    for j in range(len(month)):
        rainfall_column.append(pivot_table.iat[j, i])
        
year_column = []
for i in range(len(year)):
    for j in range(1, 13):
        year_column.append(year[i])
        
month_column = []
for i in range(len(year)):
    for j in range(1, 13):
        month_column.append(j)

# Turn into Dataframe
year_df = pd.DataFrame(year_column)
month_df = pd.DataFrame(month_column)
rainfall_df = pd.DataFrame(rainfall_column)

# Set up an empty Datafrme
final_df = pd.DataFrame()

# Put data inside
final_df['Year'] = year_df
final_df['Month'] = month_df
final_df['Rainfall (mm)'] = rainfall_df

# Output the data
final_df.to_csv('86027_output.csv', index = False)