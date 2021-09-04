# -*- coding: utf-8 -*-

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return 'Person ' + self.name +'is'+ str(self.age)
    
class Employee(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age)
        self.id=id
        
    def __str__(self):
        return  'Employee ' + self.name +'is '+ str(self.age) +'Id ' + str(self.id)
    
    
p=Person('Mukesh',39)
print(p)

e=Employee('Randy', 43,1234)
print(e)