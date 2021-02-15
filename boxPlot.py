'''
Created on Jan 31, 2021

@author: maria
'''
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')
tips = sns.load_dataset('tips')
ax = sns.boxplot(x=tips['total_bill'])
plt.title('Single horizontal boxplot')
plt.show()

