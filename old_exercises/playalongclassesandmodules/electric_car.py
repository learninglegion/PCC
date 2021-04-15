"""A class to describe an electric car and battery"""
from car import Car

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