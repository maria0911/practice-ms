'''
Created on Feb 9, 2021

@author: maria
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#load in dataset
future50_df = pd.read_csv('/Users/maria/Document/python/tuxsa/csv/future50.csv')
#set pandas to show all columns
pd.set_option("expand_frame_repr", False)
print(future50_df)

#select columns that will be used only
select_column_df = future50_df[['Restaurant', 'Sales', 'YOY_Sales']]


#remove percent sign
select_column_df['YOY_Sales'] = list(map(lambda x: x[:-1], select_column_df['YOY_Sales'].values))

#convert string to numeric value
select_column_df['YOY_Sales'] = [float(x) for x in select_column_df['YOY_Sales'].values]

#sort value from maximum on yoy_sales
sort_restaurant = select_column_df.sort_values(['YOY_Sales'], ascending=[False])

#select only the first ten restaurant after sort
sort_restaurant = sort_restaurant.head(10)
print(sort_restaurant)

#plot horizontal bar chart
ax = sort_restaurant.plot(kind='barh', x='Restaurant')
ax.set_title('Top 10 Restaurant Business Ranking 2020', pad=20, fontsize = 16)
ax.set_xticks(np.array([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]))
ax.set_xlabel('2019 Systemwide Sales ($000,000)')

#add secondary axis, position 'top'
secax = ax.secondary_xaxis('top')
secax.set_xticks(np.array([30,60,90,120,150]))
secax.set_xlabel('YOY Sales Change (%)')

plt.show()