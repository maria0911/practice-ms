'''
Created on Oct 29, 2020

@author: maria
'''
str1 = 'Hello'
print('test len function')
print(len(str1))
print('\n')

class Employees:
    #create blueprint of an instance of this class
    empCount = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Employees.empCount += 1
        
    def __len__(self):
        return len(self.name)
    
    def displayCount(self):
        print('\nTotal employees are %d' % Employees.empCount)
        
    def displayEmployee(self):
        print('Name: ', self.name, ', Year: ', self.year)
    
#create object by calling class
emp1 = Employees('Jane', 2018)
emp2 = Employees('Ron', 2016)
#call function from class
emp1.displayEmployee()
#emp1.__len__()
print(len(emp1))
emp1.displayCount()