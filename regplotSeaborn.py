'''
Created on Feb 4, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

day = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12])
money = pd.Series([5,10,13,9,16,23,10,15,8,18,28,32])
frame = {'Days': day, 'Amount of money': money}
df_money = pd.DataFrame(frame)

ax = sns.regplot(x='Days', y='Amount of money', data=df_money)
plt.title('Linear Regression in Scatter Plot')
plt.xlabel('Days')
plt.ylabel('Money ($)')
plt.show()