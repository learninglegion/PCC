# alien_0 = {'color': 'green', 'points': 5}
# alien_x = {}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just shot down a {alien_0['color']} alien! You earned {new_points} points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# aliens = {[{alien_0 = 'color': 'green', 'points': 5},{alien_1 = 'color': 'yellow', 'points': 10},{alien_2 = 'color': 'red', 'points': 15}]}
# print(aliens{alien_2['color']})
# alien_x['color'] = 'yellow'
# alien_x['points'] = 10
# print(alien_x)
# alien_0['color'] = 'yellow'
# print(f"Oh, wait, that alien was actually a {alien_0['color']} alien!")

# alien_0 = {'color': 'green', 'points': 5}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# alien_0['speed'] = 'medium'
# print(f"Original position: {alien_0['x_position']}")
# #Move the alien to the right.
# #Determine how far to move the alient based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     #This must be a fast alien.
#     x_increment = 3
# #The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# del alien_0['points']
# print(alien_0)


favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
    'alex': 'javascript',
}
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alien_0 = {'color': 'green', 'speed': 'slow'}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}!")
friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi, {name.title()}.")
#     if name in friends:
#        language = favorite_languages[name].title()
#        print(f"{name.title()}, I see you love {language}!")
#         print(f"{name.title()}, I see you love {favorite_languages[name]}!")
# if 'erin' not in favorite_languages.keys():
#     print(f"Erin, please take our poll.")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")
print("The following languages have been mentioned:")
for language in sorted(set(favorite_languages.values())):
    print(language.title())

