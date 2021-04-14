# #dog
# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """ Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.roll_over()

# #car
# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odomoter_reading = 20

#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odomoter_reading} miles on it.")
    
#     def update_odometer(self, mileage):
#         """Set the odomoter reading to the given value.
#         Reject the change if it attempts to roll the odometer back
#         """
#         if mileage >= self.odomoter_reading:
#             self.odomoter_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
    
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         if miles < 0:
#             print("Can't go backwards!")
#         else:
#             self.odomoter_reading += miles

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_used_car = Car('toyota', 'mr2', 1986)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(-100)
# my_used_car.read_odometer()

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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.fill_gas_tank()