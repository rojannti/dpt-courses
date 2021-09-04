# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 08:54:38 2019

@author: mranjan4
"""
g = 10

def fun1():
    
   
    a = 1 #a is local to function 1
    print(a)
    print(g)
    
def fun2():
    b=2 # b is local to function 2
    print(b)
    print(g)
   

fun2()


#===============================

max=100

def print_max():
    global max
    max=max+1
    print(max)
    
print_max()