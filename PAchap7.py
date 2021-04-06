#parrot
# prompt = ("\nTell me something and I will repeat it back to you: ")
# prompt += ("\nEnter 'quit' to end the program. ")
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

#greeter
# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

#rollercoaster
# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("You're tall enough to ride this ride!")
# else:
#     print("\nYou'll be able to ride when you're a little taller.")

#even_or_odd
# number = input("Enter a number and I I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

#counting
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
#
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

#cities
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you have finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"(I'd love to go to {city.title()}!")

#confirmed_users
# #Start with users that need to be verified,
# #and an empty list to hold confirmed users.
# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
# #verify each user until there are no more unconfirmed users.
# #move each verified user into the lists of confirmed users
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
# #Display all confirmed users.
# print("\nThe following users have been confirmed.")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#pets
# pets = ['dog','cat',' dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

#mountain_poll
responses = {}
#Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
#Store the response in the dictionary.
    responses[name] = response
#Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond (yes/no)? ")
    if repeat == 'no':
        polling_active = False
#Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



