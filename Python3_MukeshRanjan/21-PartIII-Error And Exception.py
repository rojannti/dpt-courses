# -*- coding: utf-8 -*-

def runcalc(x,y):
    x / y
runcalc(7,0)


# Error Code Block
try:
    runcalc(7,0)
except ZeroDivisionError:
    print('oops No Division by zero')
    
else:
    print('All code gets executed without any error')
finally:
    print('I will run everytime')
    
  

# No Error Code Block
try:
    runcalc(8,2)
except ZeroDivisionError:
    print('oops No Division by zero')
    
else:
    print('All code gets executed without any error')
    
finally:
    print('I will run everytime')