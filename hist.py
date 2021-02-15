'''
Created on Jan 28, 2021

@author: maria
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {'app_version':[1,4,2,6,5,4,5,8,
                       9,1,5,7,7,4,3,3,2]}

df = pd.DataFrame(data,columns=['app_version'])
print(df)

plt.hist(df['app_version'], bins=[0,2,4,6,8,10,12])
plt.title('Distribution of bug found in Application',
          fontsize=14)
plt.xticks([0,2,4,6,8,10,12])
plt.xlabel('Application Version', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.show()