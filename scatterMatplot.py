'''
Created on Feb 4, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import numpy as np

days = [1,2,3,4,5,6,7,8,9,10,11,12]
money = [5,10,13,9,16,23,10,15,8,18,28,32]
colors = np.random.rand(12)
plt.scatter(days, money, c=colors)
plt.title('Our jar of money each day')
plt.xlabel('Days')
plt.ylabel('Money ($)')
plt.show()