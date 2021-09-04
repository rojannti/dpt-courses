# -*- coding: utf-8 -*-


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
        
    @staticmethod
    def static_function():
        print('I am Static Method')
        
        
Person.static_function()