'''
Created on Feb 9, 2021

@author: maria
'''
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis('equal')

#load in dataset
future50_df = pd.read_csv('/Users/maria/Document/python/tuxsa/csv/future50.csv')
#set pandas to show all columns
pd.set_option("expand_frame_repr", False)
#print(future50_df)

#encoding labels
franchising_dict = {'Yes':1, 'No':2}
future50_df['Franchising'] = future50_df.Franchising.map(franchising_dict)

#select columns
select_column = future50_df[['Franchising', 'Sales', 'YOY_Sales', 'Unit_Volume']]
#print(select_column)

select_column = select_column.drop([0, 1])
#print(select_column)

#print(future50_df)
group_column = select_column.set_index('Franchising')

#remove percent sign
group_column['YOY_Sales'] = list(map(lambda x: x[:-1], group_column['YOY_Sales'].values))

#convert string to numeric value
group_column['YOY_Sales'] = [float(x) for x in group_column['YOY_Sales'].values]
#print(group_column)


df = group_column.groupby(['Franchising']).sum()

print(df)

#franchising_count = franchising_df.value_counts(sort = True)
#labels = ['Franchising', 'Not Franchising']
#print(franchising_count)


#group = group_column['YOY_Sales']
#franchising = select_column.groupby(level="Franchising")
#print(franchising)