'''
Created on Jan 15, 2021

@author: maria
'''
import pandas as pd

s = pd.Series([1,2,3,4],index=['b', 'd', 'a','c'])
print(s.reindex(['a','b','x']))

print('\n')

labels = ['a','b','x','y']
print(s.loc[s.index.intersection(labels)].reindex(labels))
s2 = pd.Series(['Anne', 'Ed', 'Ron'], index=['c', 'a', 'b'])
frame = {'Name': s2, 'no.': s}
df = pd.DataFrame(frame)
print(df)
#print(s2.sort_index)
print('\nsort index dataframe')
#print(df.sort_index())