'''
Created on Oct 29, 2020

@author: maria
'''
import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = arr1.view()

print(arr1)
print(arr2)

arr2 = (arr2 + arr1)
print('\nprint arr2 after plus each element of two arrays together and saved it as arr2')
print(arr2)


arr2 = arr2 * 2

print('\nprint arr2 after multiply each element with 2')
print(arr2)

arr2 = np.append(arr2,[5])

print('\nprint arr2 after adding one element')
print(arr2)

arr1[0] = 100
print('\nprint arr1 after changing the first element')
print(arr1)
print('\nprint arr2 after change made arr1')
print(arr2)

print('\ncreate new array suing arange range 6 and print the unique id')
a = np.arange(6)

print(id(a))
print('\nassign the a array to the b array')
b = a

print('print unique id of b array')
print(id(b))
print('\nprint the a array')
print(a)
print('can still be called')

b.shape = 3,2

print('\nchange the shape of b array then print the shape of a array')
print(a)
print('give the same shape')

x = np.arange(6).reshape(3,2)
print(x)
print(id(x))

y = x.view()
print('Shape of y: ')
print(y)
print('\nid of y: ')
print(id(y))
print('\nShape of x: ')
print(x)
print('\nid of x: ')
print(id(x))

y.shape = 2,3
print('\nNew shape of y: ')
print(y)
print('\nShape of x: ')
print(x)

y[0,1] = 33
print('\nShape of y: ')
print(y)
print('\nShape of x: ')
print(x)

z = x.copy()
z[0,1] = 44
print('\nNew shape of z: ')
print(z)
print('\nShape of x: ')
print(x) 

test = np.array([[1,2,3]])
print(test)
print(test.shape)
print(test.ndim)
