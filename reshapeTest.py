'''
Created on Nov 7, 2020

@author: maria
'''

import numpy as np

a = np.arange(1,21).reshape(5,4)
#print('print the array matrix: ')
#print(a)

'''
b = np.arange(1,25).reshape(3,2,4)
print('print the shape of b array: ')
print(b)
b = b.reshape(-1)
print('\nprint the shape of b array after reshape: ')
print(b)'''

c = np.arange(1,13)
d = c.reshape(3,2,-1)
print(d.base is None)
print(d.base is c)