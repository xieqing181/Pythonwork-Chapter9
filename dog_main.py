#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dog_main.py
#  
#  Copyright 2017 Xie Qing <xieqing@XiedeMacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    #import sys

class Dog():
    '''One trying to simulate dog'''
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        '''simulate to ask dog to sit down'''
        print(self.name.title() + " is now sitting.")
    
    
    def roll_over(self):
        '''simulate to ask dog to roll over'''
        print(self.name.title() + " rolled over!")
       
       
my_dog = Dog('jimi', 6)


print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")        

sys.exit(main(sys.argv))
