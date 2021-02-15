'''
Created on Oct 17, 2020

@author: maria
'''
#import NumPy
import numpy as np
#create structured data type
dt = np.dtype('i1')
#create array using structured data type
arr = np.array([(-1),(0),(3),(4)], dtype = dt)

print('Before converting')
print(arr)
print(arr.dtype)
print('\n')
#convert data type
newarr = arr.astype('bool')

print('after converting')
print(newarr)
print(newarr.dtype)

arr2 = np.arange(1,10,3, 'float')
print('\n')
print('use range argument function')
print(arr2)
print(arr2.dtype)

arr3 = np.arange(3)
print('\n')
print('input one argument')
print(arr3)
print(arr3.dtype)

neg = np.arange(-6, -1, -2, 'float')
print('\n')
print('input negative number, positive step')
print(neg)
print(neg.dtype)

backneg = np.arange(-1, -10, -2)
print('\n')
print('input all negative')
print(backneg)
print(backneg.dtype)

arr4 = np.arange(-6, 4, -3)
print('\n')
print('stop > start step is negative')
print(arr4)
print(arr4.dtype)

arr5 = np.arange(-6, -15, -3)
print('\n')
print('stop < start step is negative')
print(arr5)
print(arr5.dtype)

arr6 = np.abs(arr5)
print('\n')
print('get abs of arr5')
print(arr6)
print(arr6.dtype)

arr7 = np.sin(arr3)
print('\n')
print('get sin of arr3')
print(arr7)
print(arr7.dtype)

arr8 = np.arange(3)
arr8 = arr8*2
print('\n')
print('use arange with mathematical operator')
print(arr8)