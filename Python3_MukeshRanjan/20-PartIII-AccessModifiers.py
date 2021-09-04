# -*- coding: utf-8 -*-
#Example of Public Access Modifier

#Run this example seperately using Shift + Enter. To know more watch the session video

class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal


emp1=Employee("Mukesh",100000)
emp1.salary


#Example of Protected Access Modifier
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self._salary=sal
        
class payroll(Employee):
    def salgen(self):
        print ("Salary Generated")


E1=Employee('David','45345')
E1._salary

p1=payroll('David','45345')
p1._salary

#Example of Private Access Modifier
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.__salary=sal
        
    def giveEmpSalary(self):
        print(self.name,'Employee Salary is',self.__salary)
        
E2=Employee('Merry','200000')
E2.giveEmpSalary()