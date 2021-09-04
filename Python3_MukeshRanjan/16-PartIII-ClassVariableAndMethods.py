# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 04:35:07 2019

@author: mranjan4
"""

class Person:
    
    instance_count=0
    
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count+=1
    
    def __init__(self,name,age):
        Person.increment_instance_count()
        self.name = name
        self.age = age
        
    def birthday(self):
        print('Happy birthday you were', str(self.age))
        self.age+=1
        print('Your are now',self.age)
        
        
p1=Person('John',48)
p2=Person('Rohit', 33)
p3=Person('Monica', 28)

del p1,p2,p3

print(Person.instance_count)