'''
Created on Jan 26, 2021

@author: maria
'''
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)  

langs = ['English', 'Spanish', 'German', 'Russian']
students = [50, 34, 20, 28]
plt.bar(langs, students)
ax.set_ylabel('Numbers of Students')
ax.set_title('Number of students in language classes')
plt.show()