# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 00:14:47 2019

@author: mranjan4
"""

def multiply(a,b):
    return a *b

multi = multiply(2,5)

def multby(func,num):
    return lambda y: func(num,y)


double = multby(multiply,2)

print(double(5))

print(double(10))


triple = multby(multiply,3)

print(triple(5))