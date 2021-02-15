'''
Created on Feb 8, 2021

@author: maria
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#load in dataset
future50_df = pd.read_csv('/Users/maria/Document/python/tuxsa/csv/future50.csv')
#set pandas to show all columns
pd.set_option("expand_frame_repr", False)

#set a specific column to be an index
#future50_df = future50_df.set_index('Restaurant')

print(future50_df)

#select columns that will be used only
select_column_df = future50_df[['Restaurant', 'YOY_Sales']]

#remove percent sign
select_column_df['YOY_Sales'] = list(map(lambda x: x[:-1], select_column_df['YOY_Sales'].values))

#convert string to numeric value
select_column_df['YOY_Sales'] = [float(x) for x in select_column_df['YOY_Sales'].values]

print(select_column_df)

#sort value from maximum
sort_restaurant = select_column_df.sort_values(['YOY_Sales'], ascending=[False])

#select only the first ten restaurant
sort_restaurant = sort_restaurant.head(10)
print(sort_restaurant)

#plot bar chart
ax = sort_restaurant.plot(kind='barh', x='Restaurant')
  
plt.show()

