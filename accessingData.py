'''
Created on Jan 13, 2021

@author: maria
'''
import pandas as pd
import numpy as np

#create array using numpy
students = np.array(['Lily', 'Anne', 'Edmund'])
scores = np.array([7,9,8])

#create series using pandas
students_series = pd.Series(students)
scores_series = pd.Series(scores)

#create dictionary
frame = {'Student': students_series, 'Score':scores_series}

#assign dictionary to Pandas DataFrame
table = pd.DataFrame(frame)

print(table)
print('\nacc1')

#loc can put only one indexer
acc1 = table.loc[table.index[[0,1]], 'Score']
print(acc1)

print('\nacc2')

acc2 = table.iloc[table.index[[0,1]]]
print(acc2)
print('\nacc3')

acc3 = table.iloc[[0,2], table.columns.get_loc('Student')]
print(acc3)
print('\nacc4')

#if you want more than one indexer, must use iloc and explicitly specify the indexers
acc4 = table.iloc[[0,2], table.columns.get_indexer(['Student', 'Score'])]
print(acc4)

print('\nDate 15 Jan 2021\n')
print('print using loc.\n')

lst = pd.Series([3,5,2], index=['a','b','c'])
#loc must put key only. get KeyError if you put index position
acc_lst1 = lst.loc['a']
print(acc_lst1)

print('\nprint a single element using []')
#using [] can be key or indexer
acc_lst2 = lst[0]
acc_lst4 = lst['a']
acc_lst5 = lst[0:2]
print(acc_lst2, acc_lst4)
print('\n',acc_lst5)

print('\nprint using iloc\n')
#iloc must put index position only. get TypeError if you put label
acc_lst3 = lst.iloc[0:3]
print(acc_lst3)
acc_lst6 = lst.iloc[2]
print(acc_lst6)


print('\nRETURN DATAFRAME\n')

acc_lst7 = lst.loc[['a', 'b']]
print(acc_lst7)
acc_lst8 = lst.iloc[[1,2]]
print(acc_lst8)
acc_lst9 = lst[['b','c']]
print(acc_lst9)
