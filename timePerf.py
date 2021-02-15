'''
Created on Dec 3, 2020

@author: maria
'''
import numpy as np
import time

lst1 = [1,2,3]
lst2 = [4,5,6]
sum_lst = []

start = time.time()*1000000
start = int(start)
print (start)

for (i,j) in zip (lst1,lst2):
    sum_lst.append(i+j)
stop = time.time()*1000000
stop = int(stop)
print(stop)
print(sum_lst)
print(stop-start)

arr1 = np.array(lst1)
arr2 = np.array(lst2)

#start_arr = time.time()*1000000
count_start = time.perf_counter()
#start_arr = int(start_arr)
sum_arr = arr1+arr2
count_stop = time.perf_counter()
#stop_arr = time.time()*1000000
#stop_arr = int(stop_arr)

#print(sum_arr)

sum_lst = list(sum_arr)

print(sum_lst)
#print('numpy array performance: ', stop_arr-start_arr)
print(count_stop-count_start)


