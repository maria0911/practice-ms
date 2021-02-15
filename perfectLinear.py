'''
Created on Feb 1, 2021

@author: maria
'''
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12]
money = [5,10,13,17,22,25,31,35,38,43,45,50]

#slope
m = 4.2

#intercept
b = 0

#formula
y = [(m*x)+b for x in days]

#plot maker
plt.plot(days, money, 'o')
#plot line
plt.plot(days, y)

plt.title('Our jar of money')
plt.xlabel('Days')
plt.ylabel('Money ($)')

plt.show()