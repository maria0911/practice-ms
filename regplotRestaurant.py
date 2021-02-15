'''
Created on Feb 9, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#load in dataset
future50_df = pd.read_csv('/Users/maria/Document/python/tuxsa/csv/future50.csv')
#set pandas to show all columns
pd.set_option("expand_frame_repr", False)

#remove percent sign
future50_df['YOY_Sales'] = list(map(lambda x: x[:-1], future50_df['YOY_Sales'].values))

#convert string to numeric value
future50_df['YOY_Sales'] = [float(x) for x in future50_df['YOY_Sales'].values]

#remove percent sign
future50_df['YOY_Units'] = list(map(lambda x: x[:-1], future50_df['YOY_Units'].values))

#convert string to numeric value
future50_df['YOY_Units'] = [float(x) for x in future50_df['YOY_Units'].values]

print(future50_df)
#encoding labels
franchising_dict = {'Yes':1, 'No':2}
future50_df['Franchising'] = future50_df.Franchising.map(franchising_dict)

franchising_df = future50_df['Franchising']
franchising_count = franchising_df.value_counts(sort = True)

yoy_sales = future50_df['YOY_Sales']

select_column = future50_df[['Sales', 'YOY_Sales', 'Unit_Volume']]

fig, axs = plt.subplots(ncols=2)
sns.regplot(x='Sales', y='YOY_Sales', data=select_column, ax=axs[0])
sns.regplot(x='Unit_Volume', y='YOY_Sales', data=select_column, ax=axs[1])
axs[0].set_xlabel('2019 System wide Sales ($000,000)')
axs[1].set_xlabel('2019 Average Unit Volume ($000)')
axs[0].set_ylabel('YOY Sales Change (%)')
axs[1].set_ylabel('YOY Sales Change (%)')


plt.show()



