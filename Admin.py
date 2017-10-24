class User():
	'''save the user's first name, last name, and middle name,
	also some other info, like height, weight, and username.'''
	def __init__(self, first, last, height, 
	weight, username, middle=''):
		self.first = first
		self.last = last
		self.height = height
		self.weight = weight
		self.username = username
		self.middle = middle
	
	def describe_user(self):
		print("Here are some basic info about this user:\n")
		print("First name: " + self.first.title())
		print("Middle name: " + self.middle.title())
		print("Last name: " + self.last.title())
		print("Hight: " + str(self.height) + " cm")
		print("Weight: " + str(self.weight) + " kg")
		
	def greet_user(self):
		print("Hello, " + self.first.title() + self.last.title() + " !")

class Admin(User):
	'''create an new son-class named Admin, 
		def a function to show privileges of Admin'''
	def __init__(self, first, last, height, 
	weight, username, middle='', *privileges):
		super().__init__(first, last, height, 
		weight, username, middle)
		self.privileges = privileges
	
	def show_privileges(self):
		print("Welcome Admin! You can access to: ")
		for privilege in self.privileges:
			print(" - " + privilege.upper())

user1 = User('qing', 'xie', 181, 70, 'mine99')
user2 = User('jason', 'king', 178, 80, 'hero', 'william')
user3 = User('lily', 'Mosion', 165, 65, 'lilxx\'s ok', 'elisabinsh')

admin1 = Admin('adam', 'joson', 180, 90, 'nickich', 'morris', 
		'read', 'write', 'edit')

user1.describe_user()
user1.greet_user()
print("********************************")
user2.describe_user()
user2.greet_user()
print("********************************")
user3.describe_user()
user3.greet_user()
print("********************************")
admin1.describe_user()
admin1.greet_user()
admin1.show_privileges()
print("********************************")
