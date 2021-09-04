# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:56:17 2019

@author: mranjan4
"""
from functools import reduce
numbers = range(0,10)
even=[]

for i in numbers:
    if i%2 ==0:
        even.append(i)


print(even)


def is_even(x):
    return x%2 ==0

even_hof = list(filter(is_even, numbers))

print(even_hof)

#===========================

number = range (0,10)

square = list(map(lambda x : x*x, number))

print(square)

#============================

numbers = range(1,10)
reduced_value=reduce(lambda x,y:x*y,numbers)

print(reduced_value)

