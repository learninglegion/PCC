# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car =='subaru')
# print("Is car == 'audi'? I predict False.")
# print(car == 'audi')
# value = 20 * 3
# print ("Is value == 60? I predict True.")
# print (value == 60)
# person = 'MarIe'
# print("Is person.lower() == 'marie'? I predict True.")
# print(person.lower() == 'marie')
# print("Is 20 ** 2 <1000? I predict True.")
# print(20**2 < 1000)
# print("Is (value > 5) and (person.lower() == marie)? I predict True.")
# print(value > 5) and (person.lower() == marie)
# print("Is (car.upper() == 'SUBARU') or (value < 2)? I predict True.")
# print((car.upper() == 'SUBARU') or (value < 2))
# requested_toppings = ['sausage',' pepperoni','ham','bacon','beef']
# print("Is 'mushrooms' in requested_toppings? I predict False.")
# print('mushrooms' in requested_toppings)
# print("Is 'peppers' in requested_toppings? I predict False.")
# if 'peppers' not in requested_toppings:
#     print('False')
# alien_color = 'red'
# if alien_color == 'green':
#     print("The alien was green. You just earned 5 points!")
# else:
#     print("You just earned 10 points because the alien was NOT green!")
# age = 4
# if age < 2:
#     person = 'a baby'
# elif age >= 2 and age <4:
#     person = 'a toddler'
# elif age >= 4 and age <13:
#     person = 'a kid'
# elif age >= 13 and age <20:
#     person = 'a teenager'
# elif age >= 20 and age <65:
#     person = 'an adult'
# elif age >= 65:
#     person = 'an elder'
# print (f"Since you told me this person was {age} years old, I'd say this person is {person}.")
# favorite_fruits = ['blueberries','apples','oranges']
# if 'blueberries' in favorite_fruits:
#     print("You really like blueberries!")
# if 'cherries' in favorite_fruits:
#     print("You really like cherries!")
# if 'apples' in favorite_fruits:
#     print("You really like apples!")
# if 'kiwis' in favorite_fruits:
#     print("You really like kiwis!")
# if 'oranges' in favorite_fruits:
#     print("You really like oranges!")

# usernames = ['admin','brent','harry','june','stephanie']
# # usernames = []
# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print("Hello, admin! Would you like to go to the administration page?")
#         elif username in usernames:
#             print(f"Hello, {username}, what would you like to do today?")
#         else:
#             print("You are not an authorized user.")
# print("No usernames in database.")

# current_users = ['Allen','BOB','charlie','diana','elaine']
# current_users_lower = []
# new_users = ['zoe','bob','Xavier','Diana','Victoria']
# new_users_lower = []

# for cuser in current_users:
#     current_users_lower.append(cuser.lower())
# # print (current_users_lower)
# for user in new_users:
#     if user.lower() in current_users_lower:
#         print(f"Sorry, the username {user} is taken. Please try another username.")
#     else:
#         print(f"The username {user} is available!")

numbers = [1, 2, 3, 4, 5 ,6 ,7, 8, 9]
th_number = [4, 5, 6, 7, 8, 9]
st_numbers = [1]
nd_numbers = [2]
rd_numbers = [3]

for number in numbers:
    if number in th_number:
        print (f"{number}th")
    elif number in rd_numbers:
        print (f"{number}rd")
    elif number in nd_numbers:
        print (f"{number}nd")
    elif number in st_numbers:
        print (f"{number}st")








