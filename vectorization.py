'''
Created on Nov 28, 2020

@author: maria
'''

import numpy as np

#first example, stretch down

a = np.array([[1,2,3],[11,12,13],[21,22,23],[31,32,33]]) 
b = np.array([4,5,6])  

print('first arrat: \n', a)
   
print('\nsecond array: \n', b)

print('\nshape a is ', a.shape)
print('\ndimensoion is ', a.ndim)
print('\nshape b is ', b.shape)
print('\ndimension b is ', b.ndim)


x = a+b

print('\nfirst + second array: \n', x)


#second example, stretch right

arr = np.arange(12).reshape(3,4)

col_vector = np.array([5,6,7])

num_cols = arr.shape[1]

for col in range(num_cols):
    arr[:, col] += col_vector
    
print(num_cols)   
print(col_vector)
y = arr + col_vector
print(y)
    
