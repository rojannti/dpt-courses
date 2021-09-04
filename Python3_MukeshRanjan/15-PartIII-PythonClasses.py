# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:33:59 2019

@author: mranjan4
"""

class Person:
    def  __init__(self,name,age):
        self.name=name
        self.age=age
        
    def birthday(self):
        print('Happy birthday you were', str(self.age))
        self.age+=1
        print('Your are now',self.age)
        
p1 = Person('Max',40)
p2 = Person('Rambo',35)
p3 = Person('Mukesh', 39)

print(p1)

print('The name and age the of the Persion P1 is:' , p1.name, p1.age  )
print('The name and age the of the Persion P2 is:' , p2.name, p2.age  )
print('The name and age the of the Persion P2 is:' , p3.name, p3.age  )

p1.birthday()

del p1

p2.__class__