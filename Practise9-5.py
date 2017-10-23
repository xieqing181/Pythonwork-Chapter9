class User():
    '''a simulation for one user'''
    def __init__(self, first, last, username, habit, middle=''):
        self.first = first
        self.last = last
        self.username = username
        self.habit = habit
        self.middle = middle
        self.login_attemps = 0
    
    def describe_user(self):
        print("\nHere comes the information about one user: ")
        print("Name: " + self.first.title() + " " + self.middle + " " +
                self.last.title())
        print("User name: " + self.username.title())
        print("User's habit is: " + self.habit.title())
        
    def greet_user(self):
        print("Herzlich Willkommen: " + self.username.title() + " !")
        
    def increment_login_attemps(self):
        self.login_attemps += 1
        
    def reset_login_attemps(self):
        self.login_attemps = 0
    
user1 = User('qing', 'xie', 'mine99', 'basketball')
user2 = User('lily', 'Marshall', 'lilllll', 'music', 'william')

user1.describe_user()
user1.greet_user()
user1.increment_login_attemps()
print("The user login attemps is: " + str(user1.login_attemps))


user2.describe_user()
user2.greet_user()
for i in range(0,5):
    user2.increment_login_attemps()
    print("The user login attemps is: " + str(user2.login_attemps))
print("Trying to Reset user's login attemps")
user2.reset_login_attemps()
print("And now the user attemps is: " + str(user2.login_attemps))
