'''
Created on Jan 31, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

salary_data = pd.Series([30000,27000,12000,9500,19500,12000,17000,14500,24500,12000])
frame = {'Range of Salary': salary_data}
df_salary = pd.DataFrame(frame)

sns.set_theme(style='whitegrid')
ax = sns.boxplot(x=df_salary['Range of Salary'])
plt.title('Salary BoxPlot')
plt.show()