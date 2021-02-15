'''
Created on Jan 25, 2021

@author: maria
'''
import pandas as pd
import matplotlib.pyplot as plt

data = {'app_version':[1,2,3,4,5,6,7,8,9,10],
           'customer_rate': [6.3,5.5,6.2,6.5,
                             7,6.9,7.2,8,12,9.8]}

df = pd.DataFrame(data,columns=['app_version', 'customer_rate'])

plt.plot(df['app_version'], df['customer_rate'],
         color='red', marker='o')
plt.title('Customer Rate Vs Application Versions',
          fontsize=14)
plt.xlabel('Application Version', fontsize=12)
plt.ylabel('Customer Rate', fontsize=12)
plt.grid(True)
plt.show()
