class Car():
    '''a simulation for a car'''
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        
    def get_descriptive_name(self):
        long_time = str(self.year) + " " + self.make + " " + self.model
        return long_time.title()
        
    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it")

class Battery():
    
    def __init__(self, battery_size=70):
        self.battery_size = battery_size   
        
    def describe_battry(self):
        print("This car has a " + str(self.battery_size) + " -kWH battery.")
        
    def get_range(self):
        '''tell the range'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on full charge."
        print(message)
    

class ElectricCar(Car):
    '''a heritate class from Car'''
    
    def __init__(self, make, model, year):
        '''electric car, create individual methode'''
        super().__init__(make, model, year)
        #self.battery_size = 70
        self.battery = Battery()
    
    def describe_battry(self):
        print("This car has a " + str(self.battery_size) + " -kWH battery.")
            
            
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battry()
my_tesla.battery.describe_battry()
my_tesla.battery.get_range()
