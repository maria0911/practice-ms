'''
Created on Feb 1, 2021

@author: maria
'''
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12]
money = [5,10,13,9,16,23,10,15,8,18,28,32]

#m,b set1
m1 = 1
b1 = 2

#m,b set2
m2 = 2.5
b2 = 0

#m,b set3
m3 = 3
b3 = 0

#formula
y1 = [(m1*x)+b1 for x in days]
y2 = [(m2*x)+b2 for x in days]
y3 = [(m3*x)+b3 for x in days]

total_loss1 = 0
total_loss2 = 0
total_loss3 = 0

for i in range(len(money)):
    total_loss1 = (money[i]-y1[i])**2
    total_loss2 = (money[i]-y2[i])**2
    total_loss3 = (money[i]-y3[i])**2
    
print(total_loss1, total_loss2, total_loss3)

#plot marker
plt.plot(days, money, 'o')
#plot line
plt.plot(days, y1, color='r')
plt.plot(days, y2, color='g')
plt.plot(days, y3, color='m')

plt.title('Our jar of money each day')
plt.xlabel('Days')
plt.ylabel('Money ($)')

plt.show()