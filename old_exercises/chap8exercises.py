#8.1
# def display_message():
#     """Print one sentence about the material."""
#     print("I'm learning about functions. They're neat.")
# display_message()

#8.2
# def favorite_book(title):
#     """Print the title of one of my favorite books."""
#     print(f"One of my favorite books is {title.title()}.")
# favorite_book('the wastelands')

#8.3
# def make_shirt(size, text):
#     """Get parameters for a shirt to make."""
#     print(f"Ayo we need a {size} shirt with '{text.title()}' on it ASAP!")
# #make_shirt('medium', 'you can certainly try.')
# make_shirt(size='medium', text='you can certainly try.')

#8.4
# def make_shirt(size='large', text='I love Python.'):
#     """Get parameters for a shirt to make."""
#     print(f"Ayo we need a {size} shirt with '{text}' on it ASAP!")
# make_shirt()
# make_shirt(size='medium', text='You can certainly try.')

#8.5
# def describe_city(name, country='china'):
#     """List the name of a city and the country it's in."""
#     if country == 'usa' or country == 'united states':
#         print(f"{name.title()} is a city in the {country.title()}.")
#     else:
#         print(f"{name.title()} is a city in {country.title()}.")
# describe_city('beijing')
# describe_city(name='detroit', country='united states')
# describe_city(country='brazil', name='Rio')

#8.6
# def city_country(city, country):
#     """Write a city and country."""
#     location = f"{city}, {country}"
#     return location.title()
# print(city_country('evansville', 'USA'))
# place = city_country('indianapolis', 'USA')
# print(place)
# place = city_country('vincennes', 'USA')
# print(place)

#8.7
# def make_album(name, album):
#     """Describe a music album."""
#     record = {'artist_name': name.title(), 'artist_album': album.title()}
#     return record
# mjk = make_album('tool', 'lateralis')
# bh = make_album('a perfect circle', '13th step')
# tr = make_album('nin', 'broken')
# print(mjk)
# print(bh)
# print(tr)

#8.8
# def make_album(name, album):
#     """Describe a music album."""
#     record = {'artist_name': name.title(), 'artist_album': album.title()}
#     return record
# while True:
#     print("\nName some of your favorite musical artists and albums.")
#     print("(Type 'q' to quit entering info.)\n")
#     given_name = input("First, give me the name of a band or artist: ")
#     if given_name == 'q':
#         break
#     given_album = input("Now give me the name of one of their albums: ")
#     if given_album == 'q':
#         break
#     cd = make_album(given_name, given_album)
#     print(cd)

#8.9 - 8.10 - 8.11
# messages = ['hi!','whats up?','how are you?']
# sent_messages = []
# def show_messages(message):
#     for message in messages:
#         print(message)
# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)
# send_messages(messages[:], sent_messages)
# print(messages)
# print(sent_messages)

#8.12
# def sandwich(*toppings):
#     print("Sandwich order ready. This sandwich has:")
#     for topping in toppings:
#         print(f"- {topping}")
# sandwich('ham')
# sandwich('ham', 'cheese')
# sandwich('ham', 'cheese', 'bacon')

#8.13
# def build_profile(first, last, **user_info):
#     """Build a dictionary with everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('brent', 'beckwith',
#                             location ='aurora',
#                             field = 'information technology',
#                             country = 'USA')
# print(user_profile)

#8.14
# def make_car(manufacturer, model, **kwargs):
#     """Store info about a car"""
#     kwargs['car_make'] = manufacturer
#     kwargs['car_model'] = model
#     return kwargs
# car_info = make_car('Toyota', 'MR2',
#                 color='red',
#                 engine='4 cylinder',
#                 brakes='ABS')
# print(car_info)

#8.15
# import printing_functions as pf
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_models = []
# pf.print_models(unprinted_designs[:], completed_models)
# pf.show_completed_models(completed_models)
# print(unprinted_designs)

#8.16
import car_creator
from car_creator import make_car
from car_creator import make_car as mc
import car_creator as cc
from car_creator import *

