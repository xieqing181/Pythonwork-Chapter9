#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Practise9-1.py
#  
#  Copyright 2017 Xie Qing <xieqing@XiedeMacBook-Air.local>

class Restaurant():
    '''创建一个类 - 餐馆，包含name和cuisine方法'''
    def __init__(self, name, cuisine_type, open_time):
        self.name = name
        self.cuisine_type = cuisine_type
        self.open_time = open_time
        
    def describe_restaurant(self):
        print("The restaurant's name is: " + self.name.title())
        print("\nAnd the cuisine type is: " + self.cuisine_type.upper())
    
    def open_restaurant(self):
        print("\nThe open time is: " + self.open_time.upper())

restaurant = Restaurant('jimi\'s back', 'asia', '9am - 10pm')
print("Now let see the restaurant: ")
print("The name is: " + restaurant.name.title() 
        + " And cuisine is: " + restaurant.cuisine_type.upper())
restaurant.describe_restaurant()
restaurant.open_restaurant()
