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
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
x = 1
while x <= 5:
    print(x)
    x += 1



#cities
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you have finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"(I'd love to go to {city.title()}!")