"""A module to define restauarants"""

class Restaurant:
    """An attempt to define a restuarant."""

    def __init__(self, name, cuisine):
        """initializing the restaurant class"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 10

    def describe_restaurant(self):
        """Describe the retaurant"""
        print(f"{self.name} is the epitome of {self.cuisine} food!")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"{self.name} is now open for business!")

    def read_number_served(self):
        """Cite number of patrons served."""
        print(f"We've served {self.number_served} people!")
    
    def set_number_served(self, visitors):
        """Set the number of people served."""
        if visitors >= self.number_served:
            self.number_served = visitors
        else:
            print("We aren't time travelers, you can't rescind your visit!")

    def increment_number_served(self, new_customers):
        """Increase the number of people served."""
        if new_customers > 0:
            self.number_served += new_customers
        else:
            print("You can't have negative people.")

class IceCreamStand(Restaurant):
    
    def __init__(self, name, cuisine):
        """initializing the icecreamstand class"""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry', 'rocky road']

    def display_flavors(self):
        print(f"We have the following flavors:")
        for flavor in self.flavors:
            print(flavor.title())