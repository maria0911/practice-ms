'''
Created on Jan 31, 2021

@author: maria
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('http://bit.ly/2cLzoxH')
#subset the data frame for 2 rows of year value
df1 = data[data['year'].isin([1952,2007])]

sns.boxplot(y='lifeExp', x='continent', data=df1, hue='year')
plt.title('Grouped Boxplot of Life Expectancy')
plt.ylabel('Life Expectancy')
plt.xlabel('Continent')
plt.show()

