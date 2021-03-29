# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')
# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
# banned_users = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish")
# age = 17
# if age >=18:
#     print("You're old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you're too young to vote.")
#     print("Please register to vote as soon as you turn 18!")
# age = 62
# if age <4:
#     print("Your admission cost is $0")
# elif age <18:
#     print("Your admission cost is $25")
# else:
#     print("Your admission cost is $40")
# if age <4:
#     price = 0
# elif age <18:
#     price = 25
# elif age >=65:
#     price = 20
# else:
#     price =40
# print(f"Your admission cost is ${price}.")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
# requested_toppings = []
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms.')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni.')
# if 'beef' in requested_toppings:
#     print('Adding beef.')
# print("\nFinished making your pizza!")
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"You want some {requested_topping} on that?")
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print (f"Uhhh, sorry we don't have {requested_topping}.")
    print("Your pizza is ready!")
else:
    print("\nAre you sure you want a plain cheese pizza?")