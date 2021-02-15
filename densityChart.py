'''
Created on Jan 29, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

salary = pd.Series([30000,27000,12000,9500,19500,12000,17000,14500,24500,12000])
frame = {'Range of Salary': salary}
df_salary = pd.DataFrame(frame)
sns.set_style('whitegrid')
sns.distplot(df_salary)
#sns.displot(data=df_salary,x='Range of Salary', kind='ecdf')
plt.title('Density of Salary',
          fontsize=14)
plt.show()