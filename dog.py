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
       
       
my_dog = Dog('willile', 6)
your_dog = Dog('jimi', 8)

print("My dog's name is " + my_dog.name.title())
print("My dog is " + str(my_dog.age) + " years old.")        
my_dog.sit()
my_dog.roll_over()

print(your_dog.name + " is your dog, right?")
print("And its age is: " + str(your_dog.age))
your_dog.sit()
your_dog.roll_over()
