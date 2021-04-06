#7.1
# rental_car = input("Need a rental car, eh? What kind of car would you like to drive? ")
# print(f"Let me see if I have any {rental_car}s available.")

#7.2
# group = input("Welcome to Brenty's! How many are in your party? ")
# group = int(group)
# if group > 8:
#     print("Large party! You'll need to wait a bit for a table to open up.")
# else:
#     print("Great! We have a table ready for you. Please follow me.")

#7.3
# number = input("Tell me a number and I'll let you know if it's divisible by 10: ")
# number = int(number)
# if number % 10 == 0:
#     print(f"Yep, {number} is divisible by 10.")
# else:
#     print(f"{number} is not divisible by 10.")

#7.4
# toppings = []
# prompt = "Build your pizza! One topping at a time."
# prompt += "\nType 'quit' when finished.\n"
# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False        
#     else:
#         toppings.append(topping)
#         print(f"Got it. You want {topping}.")
# print(f"Here's a list of your toppings:{toppings}")
# 7.6
# toppings = []
# prompt = "Build your pizza! One topping at a time and up to five toppings."
# prompt += "\nType 'quit' when finished.\n"
# while len(toppings) < 6:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     elif len(toppings) == 5:
#         print("Five toppings is all you get!")
#         break
#     else:
#         toppings.append(topping)
#         print(f"Got it. You want {topping}.")
# print(f"Here's a list of your toppings:{toppings}")

#7.5
prompt = "Welcome to the movies! We charge based on age.\n"
prompt += "Tell me how old you are and I'll tell you how much a ticket costs.\n"
age = input(prompt)
age = int(age)
if age < 3:
    print("Babies don't even know what movies are. You get in free!")
elif age >= 3 and age <= 12:
    print("Ah, one kids ticket. $10 please.")
else:
    print("Thirteen or over I see. Adult tickets are $15.")

#7.7 - INFINITE LOOP
# x = 1
# while x <3:
#     print(x)




