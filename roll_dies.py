from random import randint

class Die():
	def __init__(self, sides = 6):
		'''def a die with 6 sides'''
		self.sides = sides 
		
	def roll_die(self):
		x = randint(1,self.sides)
		return x


die_6sides = Die()
for i in range(1,11):
	print(str(i)+ " time trying: " + str(die_6sides.roll_die()))
	
die_10sides = Die(10)
print("\n Show the 10 sides dies result:")
for i in range(1,11):
	print(str(i)+ " time trying: " + str(die_10sides.roll_die()))
	
die_20sides = Die(20)
print("\n Show the 20 sides dies result:")
for i in range(1,11):
	print(str(i)+ " time trying: " + str(die_20sides.roll_die()))

