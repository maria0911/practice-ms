'''
Created on Dec 22, 2020

@author: maria
'''
import pandas as pd
import numpy as np

subjects = ['math', 'eng', 'sci']
subjects_series = pd.Series(subjects)
grades_series = pd.Series(['C','A','B'])
frame = {'Subject':subjects_series, 'Grade':grades_series}
table = pd.DataFrame(frame)
print(table)

scottish_hills = pd.read_csv('/Users/maria/Document/python/CC-python-pandas-matplotlib-master/scottish_hills.csv')

nba_players = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/nba.csv')
scottish_hills.dropna()
perc = [.20, .40, .60, .80]
include = ['object', 'int', 'float']

print(scottish_hills.describe(percentiles = perc))


scores_series = pd.Series([4, 6, 5, 9, 8, 2,7])
print(scores_series.describe())

print('\nData Accessing\n')

score = [5,6,8,4,7]
print('Print score: ', score)

score_series = pd.Series(score, index=[10,11,12,13,14])
print('\nPrint score as Series: \n', score_series)
#print('Accessing element in Series score index 4: ', score_series[4])

#print(score_series[11, 12, 13])
# creating simple array 
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data, index =[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]) 
   
   
# accessing a multiple element using  
# index element 
#print(score_series[[10, 12, 14, 15, 16]])
s = score_series.loc[[11,12,13]]

print(s)

