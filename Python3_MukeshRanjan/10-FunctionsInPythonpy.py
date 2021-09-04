# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 06:09:39 2019

@author: mranjan4
"""

def Addition(input1,input2=5):
    return input1+input2

def Substraction(input1,input2):
    return input1-input2

def Multiply(input1,input2):
    return input1*input2

def Division(input1,input2):
    return input1/input2


def multiAddition(*args):
    total=0
    for i in args:
        total+=i
        
    return total

Add = Addition(input2=7,input1=2)
print(Add)

Substract = Substraction(3,2)
print(Substract)

Multi = Multiply(3,3)
print(Multi)

Divide = Division(9,3)
print(Divide)

addnvalue=multiAddition(2,3,4,5,6,7,8,9)
print(addnvalue)


#==========

def named(**kwargs):
    for key in kwargs.keys():
        print('arg:',key, 'has value:',kwargs[key])

named(a=1,b=2,c=3)

named(a=1,b=2,c=3,d=4,e=5)


# lambda arguments: expression

double = lambda i : i*i

print(double(10))













