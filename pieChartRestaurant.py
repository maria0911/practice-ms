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
print(future50_df)

#select niminal data
select_frachising = future50_df[['Franchising']]
print(select_frachising)

#encoding labels
franchising_dict = {'Yes':1, 'No':2}
select_frachising['Franchising'] = select_frachising.Franchising.map(franchising_dict)
print(select_frachising)

#create dataframe of one column
franchising_df = select_frachising['Franchising']

#count number of franchises
franchising_count = franchising_df.value_counts(sort = True)
labels = ['Franchising', 'Not Franchising']
print(franchising_count)

#plot pie chart
ax.pie(franchising_count, labels=labels, autopct='%.2f%%')
plt.legend(title = 'Franchise or Not')
ax.set_title('Top 50 Restaurant Business Ranking 2020', pad=20, fontsize = 16)
#lt.show()
