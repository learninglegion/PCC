# known_person = {
#     'first_name': 'alex',
#     'last_name': 'shelton',
#     'age': '22',
#     'city': 'willoughby',
# }
# print(known_person)

# people_numbers = {
#     'stephanie': '55',
#     'dragon': '7',
#     'sean': '123',
#     'patrick': '4',
#     'matt': '22',
# }
# for name in people_numbers:
#     print(f"The favorite number of {name} is {people_numbers[name]}!")

# programming_words = {
#     'del': 'a method used to remove data from a list or dictionary.',
#     'get': 'a method used to provide a value if no key exists in a dictionary.',
#     'title': 'a method used to capitalize the first letter of the object.',
#     'append': 'a method used to add data to a list',
#     'tuple': 'an unmodifiable list.',
#     'if/else': 'a way to define actions to take through a statement or loop',
#     'loop': 'an algorithm used to iterate through a list of items.',
#     'list': 'a modifiable list of values.',
#     'dictionary': 'a paired key/value list.',
#     'set': 'a list run through the unique filter.',
#     'len': 'a method used to print the length of a list, tuple, dictionary, etc.',
# }
# for word, definition in programming_words.items():
#     print(f"{word.title()} is {definition}\n")

# rivers = {
#     'mississippi': 'usa',
#     'nile': 'egypt',
#     'amazon': 'brazil',
#     }
# for river, country in rivers.items():
#     if country != 'usa':
#         print(f"The {river.title()} runs through {country.title()}")
#     if country == 'usa':
#         print(f"The {river.title()} runs through {country.upper()}")
# for name in rivers.keys():
#     print(name.title())
# for country in rivers.values():
#     print(country.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'ruby',
#     'phil': 'python',
#     'alex': 'javascript',
#     }
# poll_missers = ['stephanie','john','alex','xavier','sarah','jen']
# for name in poll_missers:
#     if name in favorite_languages.keys():
#         language = favorite_languages[name]
#         print(f"Thanks for taking the poll, {name.title()}. Good luck with {language.title()}!")
#     else:
#         print(f"{name.title()} quit procrastinating and take the damn poll. Geez.")

# people = []
# person_1 = {'first_name': 'alex',
#     'last_name': 'shelton',
#     'age': '22',
#     'city': 'willoughby',}
# person_2 = {'first_name': 'stephanie',
#     'last_name': 'shelton',
#     'age': '47',
#     'city': 'aurora',}
# person_3 = {'first_name': 'dragon',
#     'last_name': 'shadow',
#     'age': '44',
#     'city': 'evansville',}
# people.append(person_1)
# people.append(person_2)
# people.append(person_3)
# for person in people[:]:
#     print(person)
# # for full_name, info in people.items():
# #     full_name = f"{people['first_name']} {people['last_name']}"
# #     print(f"{person.title()} is {people['age']} years old and lives in {people['city']}.")

# pets = []
# pet_1 = {'name': 'dapper',
#     'species': 'dog',
#     'owner': 'stephanie',}
# pet_2 = {'name': 'speedy',
#     'species': 'turtle',
#     'owner': 'brent',}
# pet_3 = {'name': 'francis',
#     'species': 'parrot',
#     'owner': 'george',}
# pets.append(pet_1)
# pets.append(pet_2)
# pets.append(pet_3)
# for pet in pets:
#     print(pet)

# favorite_places = {
#     'matt': {
#     'place_1': 'bloomington',
#     'place_2': 'evansville',
#     'place_3': 'work',
# },
#     'marshall': {
#     'place_1': 'evansville',
#     'place_2': 'indianapolis',
#     'place_3': 'muncie',
# },
#     'sean': {
#     'place_1': 'san jose',
#     'place_2': 'trenton',
#     'place_3': 'st. louis',
#     },
# }
# for name, place in favorite_places.items():
#     places = f"{place['place_1']}, {place['place_2']}, {place['place_3']}"
#     print(f"{name.title()}'s favorite places are:")
#     print(f"{places.title()}.\n")







