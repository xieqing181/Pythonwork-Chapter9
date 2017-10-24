class Restaurant():
	'''build a class named Restaurant, to 
	save some info of restaurant. 
	making son-class IceCreamStand'''
			
	def __init__(self, restaurant_name, cuisine_type, open_time):
		self.name = restaurant_name
		self.cuisine_type = cuisine_type
		self.open_time = open_time
		self.number_served = 0
		
	def describe_restaurant(self):
		print("The name of the restaurant is: " + self.name.title())
		print("And the cuisine type is: " + self.cuisine_type.upper())
	
	def open_restaurant(self):
		print("The open time is below:")
		print(" - " + self.open_time.upper())
		
	def set_number_served(self, number_customer):
		self.number_served = number_customer
		
	def increment_number_served(self, number_customer_increased):
		self.number_served += number_customer_increased


'''def an new son-class icecreamstand'''

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, open_time, *flavors):
		super().__init__(restaurant_name, cuisine_type, open_time)
		self.flavors = flavors
		
	def print_flavors(self):
		for flavor in self.flavors:
			print("We " + self.name.title() + " have " + flavor.title() + " flavors Icecreams here!")
		
	
'''def function to print out Restaurant infomation'''

def print_restaurant(restaurant_name):	
	'''def a function to print out restaurant info'''
	print("********----------------*************")
	restaurant_name.describe_restaurant()
	restaurant_name.open_restaurant()
	print("Willkommen zu " + restaurant_name.name)
	
def print_number_served(restaurant_name):
	print("Till now " + str(restaurant_name.number_served) + 
            " guests have eaten in this restaurant!")
	#restaurant_name.increment_number_served(number_customer_increased)
    
def print_number_increment(restaurant_name):
	print("And after ONE hour, the total customers are:" 
			+ str(restaurant_name.number_served))

myrestaurant = Restaurant('jimi\'s back', 'mexsico', '9am till 10 pm')
print_restaurant(myrestaurant)

your_restaurant = Restaurant('fishermann', 'Turkish', '6pm - 12pm')
your_restaurant.number_served = 100
print_restaurant(your_restaurant)
print_number_served(your_restaurant)
your_restaurant.increment_number_served(222)
print_number_increment(your_restaurant)


her_restaurant = Restaurant('qiuqiu', 'chinese', '6am to 12am')
her_restaurant.set_number_served(211)
print_restaurant(her_restaurant)
print_number_served(her_restaurant)
her_restaurant.increment_number_served(999)
#print_restaurant(her_restaurant)
print_number_increment(her_restaurant)


'''Create a example to get icecream favors print out'''
icecream_restaurant = IceCreamStand('Mojito', 'Italien', '10am - 12pm', 'honey', 'nuts')

print_restaurant(icecream_restaurant)
icecream_restaurant.print_flavors()
