# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 21:01:54 2019

@author: mranjan4
"""
#Creating a dictionary
cities = {
           'wales':'Cardiff',
           'England':'London',
           'Scotland': 'Edinburgh',
          
        
        }

#===========================

print(cities['wales'])


dict1={}

#Adding a New Entry

cities['France'] = 'Paris'

#===========================
#changing the value by using keys
cities['Wales']='Cardiff1'

cities['wales']='Cardiff2'


#===========================
#Remove Entry
cities.pop('Wales')