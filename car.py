"""A class that can be used to represent a car."""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odomoter_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odomoter reading to the given value.
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