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
number = input("Tell me a number and I'll let you know if it's divisible by 10: ")
number = int(number)
if number % 10 == 0:
    print(f"Yep, {number} is divisible by 10.")
else:
    print(f"{number} is not divisible by 10.")