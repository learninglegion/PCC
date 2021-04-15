# #9.1
# class Restaurant:
#     """An attempt to define a restuarant."""

#     def __init__(self, name, cuisine):
#         """initializing the restaurant class"""
#         self.name = name
#         self.cuisine = cuisine

#     def describe_restaurant(self):
#         """Describe the retaurant"""
#         print(f"{self.name} is the epitome of {self.cuisine} food!")

#     def open_restaurant(self):
#         """Open the restaurant"""
#         print(f"{self.name} is now open for business!")

# my_restaurant = Restaurant('bojo', 'chinese')
# print(my_restaurant.name)
# print(my_restaurant.cuisine)
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# #9.2.
# s_restaurant = Restaurant('mojo', 'mexican')
# s_restaurant.describe_restaurant()
# d_restaurant = Restaurant('hojo', 'american')
# d_restaurant.describe_restaurant()

# #9.3
# class User:
#     def __init__(self, first_name, last_name, username, password, access_level):
#         """initialize the user"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.password = password
#         self.access_level = access_level

#     def describe_user(self):
#         """describe the user"""
#         print(f"Acessing database for {self.username}:\n")
#         print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")
#         print(f"Password: {self.password} Access level: {self.access_level}")
        
#     def greet_user(self):
#         """Greet the user on login"""
#         print(f"Hello again, {self.username}.")
# my_user = User('brent', 'beckwith', 'bbeckwith', 'qweqwe', 'admin')
# s_user = User('stephanie', 'shelton', 'sshelton', '2wires', 'read-only')
# a_user = User('alex', 'shelton', 'ashelton', 'nspyugiogrumps', 'programmer')
# my_user.describe_user()
# my_user.greet_user()
# s_user.describe_user()
# s_user.greet_user()
# a_user.describe_user()
# a_user.greet_user()

# #9.4
# class Restaurant:
#     """An attempt to define a restuarant."""

#     def __init__(self, name, cuisine):
#         """initializing the restaurant class"""
#         self.name = name
#         self.cuisine = cuisine
#         self.number_served = 10

#     def describe_restaurant(self):
#         """Describe the retaurant"""
#         print(f"{self.name} is the epitome of {self.cuisine} food!")

#     def open_restaurant(self):
#         """Open the restaurant"""
#         print(f"{self.name} is now open for business!")

#     def read_number_served(self):
#         """Cite number of patrons served."""
#         print(f"We've served {self.number_served} people!")
    
#     def set_number_served(self, visitors):
#         """Set the number of people served."""
#         if visitors >= self.number_served:
#             self.number_served = visitors
#         else:
#             print("We aren't time travelers, you can't rescind your visit!")

#     def increment_number_served(self, new_customers):
#         """Increase the number of people served."""
#         if new_customers > 0:
#             self.number_served += new_customers
#         else:
#             print("You can't have negative people.")

# my_restaurant = Restaurant('bojo', 'chinese')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# my_restaurant.read_number_served()
# my_restaurant.set_number_served(50)
# my_restaurant.read_number_served()
# my_restaurant.increment_number_served(25)
# my_restaurant.read_number_served()

# #9.5
# class User:
#     def __init__(self, first_name, last_name, username, password, access_level):
#         """initialize the user"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.username = username
#         self.password = password
#         self.access_level = access_level
#         self.login_attempts = 0

#     def describe_user(self):
#         """describe the user"""
#         print(f"Acessing database for {self.username}:\n")
#         print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")
#         print(f"Password: {self.password} Access level: {self.access_level}")
        
#     def greet_user(self):
#         """Greet the user on login"""
#         print(f"Hello again, {self.username}.")
    
#     def increment_login_attempts(self):
#         """Increase numberof login attempts"""
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         """Set login attempts back to 0"""
#         self.login_attempts = 0


# my_user = User('brent', 'beckwith', 'bbeckwith', 'qweqwe', 'admin')
# # s_user = User('stephanie', 'shelton', 'sshelton', '2wires', 'read-only')
# # a_user = User('alex', 'shelton', 'ashelton', 'nspyugiogrumps', 'programmer')
# my_user.describe_user()
# my_user.greet_user()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# my_user.increment_login_attempts()
# print(f"You attempted to login {my_user.login_attempts} times.")
# my_user.reset_login_attempts()
# print(f"You attempted to login {my_user.login_attempts} times.")
# # s_user.describe_user()
# # s_user.greet_user()
# # a_user.describe_user()
# # a_user.greet_user()

# #9.6 - requires restaurant class to be live
# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine):
#         """initializing the icecreamstand class"""
#         super().__init__(name, cuisine)
#         self.flavors = ['chocolate', 'vanilla', 'strawberry', 'rocky road']

#     def display_flavors(self):
#         print(f"We have the following flavors:")
#         for flavor in self.flavors:
#             print(flavor.title())

# my_stand = IceCreamStand('baskin robins', 'ice cream')
# my_stand.display_flavors()

# #9.7 - requires 9.3 to be live
# class Admin(User):
#     def __init__(self, first_name, last_name, username, password, access_level):
#         """initialize the admin"""
#         super().__init__(first_name, last_name, username, password, access_level)
#     #     self.privileges = ['can add post', 'can delete post', 'can ban user']
#         self.privileges = Privileges()
    
    # def show_privileges(self):
    #     """show the privileges an admin has"""
    #     print(f"An admin has the following privileges:")
    #     for privilege in self.privileges:
    #         print(privilege)
# my_admin = Admin('brent', 'beckwith', 'bbeckwith', 'qweqwe', 'admin')
# my_admin.show_privileges()

# #9.8 - requires 9.7 to be live but privileges commented
# class Privileges:
#     """Outline the privileges an admin has."""
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user']

#     def show_privileges(self):
#         """show the privileges an admin has"""
#         print(f"An admin has the following privileges:")
#         for privilege in self.privileges:
#             print(privilege)

# my_admin = Admin('brent', 'beckwith', 'bbeckwith', 'qweqwe', 'admin')
# my_admin.privileges.show_privileges()

#9.9
#electric car - inheritance
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 20

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odomoter_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """Set the odomoter reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odomoter_reading:
            self.odomoter_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("Can't go backwards!")
        else:
            self.odomoter_reading += miles
    
    def fill_gas_tank(self):
        """Fill the car gas tank"""
        long_name = f"{self.year} {self.make} {self.model}"
        print(f"You've just filled the {long_name.title()}'s gas tank!")

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_used_car = Car('toyota', 'mr2', 1986)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-100)
# my_used_car.read_odometer()

class Battery:
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """upgrade battery size to 100 if it isnt already"""
        print(f"Let's see if we can upgrade this {self.battery_size}-kWh battery.")
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"You were old and busted, now you have a 100-kWh battery!")
        else:
            print("You've got the best already, baby!")

class ElectricCar(Car):
    """Represents apects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of PARENT class.
        THEN initialize attributes specfic to an electric car"""
        super().__init__(make, model, year)
        # self.battery_size = 75 - before battery was made its own class
        self.battery = Battery() #now the new class is called instead

    # before battery was made its own class
    # def describe_battery(self):
    #     """Print a statement describing battery size"""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Fill the car gas tank"""
        print(f"Electic cars don't have gas tanks!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
