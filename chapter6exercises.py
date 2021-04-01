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

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    'alex': 'javascript',
    }
poll_missers = ['stephanie','john','alex','xavier','sarah','jen']
for name in poll_missers:
    if name in favorite_languages.keys():
        language = favorite_languages[name]
        print(f"Thanks for taking the poll, {name.title()}. Good luck with {language.title()}!")
    else:
        print(f"{name.title()} quit procrastinating and take the damn poll. Geez.")












