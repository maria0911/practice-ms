'''
Created on Jan 27, 2021

@author: maria
'''

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis('equal')

langs = ['English', 'Spanish', 'German', 'Russian']
students = [50, 34, 20, 28]
explode = [0.12, 0, 0.1, 0]
ax.pie(students, labels = langs, autopct='%.2f%%', explode = explode, startangle = 90)
plt.legend(title = 'Languages')
plt.show()