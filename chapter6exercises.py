known_person = {
    'first_name': 'alex',
    'last_name': 'shelton',
    'age': '22',
    'city': 'willoughby',
}
print(known_person)

people_numbers = {
    'stephanie': '55',
    'dragon': '7',
    'sean': '123',
    'patrick': '4',
    'matt': '22',
}
for name in people_numbers:
    print(f"The favorite number of {name} is {people_numbers[name]}!")

programming_words = {
    'del': 'a method used to remove data from a list or dictionary.',
    'get': 'a method used to provide a value if no key exists in a dictionary.',
    'title': 'a method used to capitalize the first letter of the object.',
    'append': 'a method used to add data to a list',
    'tuple': 'an unmodifiable list.',
}
for word in programming_words:
    print(f"{word.title()} is {programming_words[word]}\n")