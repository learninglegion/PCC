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