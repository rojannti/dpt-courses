# -*- coding: utf-8 -*-


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def birthday(self):
        print('Happy Birthdy you were',self.age)
        self.age+=1
        print('You are now', self.age)
        
        

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name,age)
        self.id=id
        
    def calculate_pay(self,hours_worked):
        rate_of_pay = 8.50
        if self.age >=21:
            rate_of_pay +=2.50
        return hours_worked * rate_of_pay
    
class SalesPerson(Employee):
    def __init__(self,name,age,id,region,sales):
        super().__init__(name,age,id)
        self.region=region
        self.sales=sales
        
    def bonus(self):
        return self.sales*0.6
    
    
#Create objects of Classes
        
print('Person')
p = Person('Mukesh',39)
print(p.name,"is",p.age)
print("=" * 25)

print('Employee')
e=Employee('Monica', 28,8989)
e.birthday()
print('e.calcualte_pay(40)', e.calculate_pay(40))
print("="*25)

print('SalesPerson')
s=SalesPerson('Jack',34,6712,'UK',40000.0)
s.birthday()
print('e.calcualte_pay(40)', s.calculate_pay(40))
print('s.bonus()',s.bonus())

