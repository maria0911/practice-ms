'''
Created on Nov 20, 2020

@author: maria
'''
import time
from time import struct_time

seconds = time.time()
print('seconds since epoch is', seconds)
local_time = time.ctime()
print('\nlocal time is: ', local_time)

print('\nThe next thread will be suspended for 3 seconds')
#time.sleep(3)
print('Appeared after 3 seconds')

time_tuple =(2018, 12, 27, 6, 35, 17, 3, 361, 0)
time_obj = struct_time(time_tuple)
print('\ntime in tuple', time_obj)
day_of_week = time_obj.tm_wday
print('day of week: ', day_of_week)
day_of_year = time_obj[7]
print('day of year: ', day_of_year)

time_local = time.localtime()
print('\ngmt', time_local)
print('gmt hour: ', time_local.tm_hour)
print('gmt day: ', time_local.tm_wday)

time_utc = time.gmtime()
print('\nutc time struct time: ', time_utc)
print('utc hour: ', time_utc.tm_hour)
print('utc day: ', time_utc.tm_wday)

local_inverse = time.mktime(time_tuple)
print('\nconverse time tuple into seconds since epoch of local time: ', local_inverse)

seconds_test = 1545867317.0
converse_to_gmt = time.localtime(seconds_test)
print('\nconverse seconds test time into gmt ', converse_to_gmt)

converse_to_utc = time.gmtime(seconds_test)
print('\nconverse seconds test time into utc ', converse_to_utc)

time_string = time.asctime()
print('\ntime string gave the same result as ctime which is: ', time_string)

time_format = time.strftime('%d-%m-%y %H:%M:%S', time.localtime())
print('\nformatting local time: ', time_format)

str_to_struct = time.strptime('25 January 1994', '%d %B %Y')
print('\nstruct time of string time: ', str_to_struct)
