'''
Created on Jan 19, 2021

@author: maria
'''
import csv
import pandas as pd
import numpy
from numpy import nan as NA

data_list = [['Name', 'Profession', 'Age'],
             ['Anne', 'Software Developer', 29],
             ['Paul', 'Manager', 35],
             ['Derek', 'software Developer', NA]]
with open('persons.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data_list)

#persons = pd.read_csv('/Users/maria/Document/python/tuxsa/persons.csv')
#print(persons)

with open('/Users/maria/Document/python/tuxsa/persons.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    df = pd.DataFrame([csv_reader], index = None)
    
    
        

persons = pd.read_csv('/Users/maria/Document/python/tuxsa/persons.csv')
print(persons)
print('\nPrint Derek DataFrame\n')
print(persons['Age'])
print(persons['Age'].isnull())
print('\nreplace na value\n')
persons['Age'].fillna(32, inplace = True)
print(persons)

data_list2 = [['code', 'name', 'age', 'email'],
              ['--', 'Lily', 23, 'lily@email.com'],
              [NA, 'Jen', 28, 'jen@email.com'],
              [462, 'Eddie','n/a']]
with open('employees.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(data_list2)

print('\nPrint employees table')
employees = pd.read_csv('/Users/maria/Document/python/tuxsa/employees.csv')
print(employees)

missing_values = ['--']
employees = pd.read_csv('/Users/maria/Document/python/tuxsa/employees.csv', na_values = missing_values)
print(employees.isnull().sum())


