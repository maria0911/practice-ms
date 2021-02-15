'''
Created on Jan 27, 2021

@author: maria
'''
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)

arr_women = np.array([30, 9, 13, 14])
arr_men = np.array([20, 15, 7, 14])
arr_students = arr_women + arr_men
women = list(arr_women)
men = list(arr_men)
langs = ['English', 'Spanish', 'German', 'Russian']

ax1.bar(langs, women, bottom = men, color='#fe793d')
ax1.bar(langs, men, color='#95bddc')
ax1.set_ylabel('Number of students')
ax1.legend(labels=['Women', 'Men'])
ax1.set_title('Number of all students in language classes')

ax2.bar(langs, women, color='#fe793d')
ax2.set_ylabel('Number of students')
ax2.set_title('Number of female students')

ax3.bar(langs, men, color='#95bddc')
ax3.set_ylabel('Number of students')
ax3.set_title('Number of male students')

plt.show()