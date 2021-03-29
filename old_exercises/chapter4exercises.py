# pizzas = ['sausage', 'bacon', 'the works']
# for pizza in pizzas:
#     print(f"{pizza.title()} pizza is pretty good!")
# print("Pizza is ok. I try not to eat too much.")
# animals = ['octopus', 'raven', 'chimpanzee']
# for animal in animals:
#     print (f"If you like smart animals, you'd like a {animal.title()}!")
# print("Any of these animals may rule the world after humans die!")
# for value in range(1, 21):
#     print(value)
# numbers = range(1, 1000001)
# for value in numbers:
#     print(value)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# numbers = range(3, 31, 3)
# for value in numbers:
#     print(value)
# cubes = []
# for value in range (1, 11):
#     cubes.append(value**3)
#     print(cubes[-1])
# cubes = [value**3 for value in range(1, 11)]
# print(cubes)
# pizzas = ['sausage', 'bacon', 'the works','pepperoni','cheese']
# print(f"The first three pizzas on the list are {pizzas[:3]}.")
# print(f"The middle three pizzas on the list are {pizzas[1:4]}.")
# print(f"The last three pizzas on the list are {pizzas[-3:]}.")
# friend_pizzas = pizzas[:]
# pizzas.append('ham')
# friend_pizzas.append('turkey')
# print("My favorite pizzas are:")
# for pizza in pizzas:
#     print(pizza[:])
# print("My friends favorite pizzas are:")
# for fpizza in friend_pizzas:
#     print(fpizza[:])
# my_foods = ['pizza','falafel','carrot cake']
# #You need a slice so that you don't equate the variables.
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# for food in my_foods:
#     print(food[:])
# print("My friends favorite foods are:")
# for ffood in my_foods:
#     print(ffood[:])
# buffet_foods = ('steak','potatoes','brocolli','rice','chicken')
# print("These are the buffet foods:")
# for bfood in buffet_foods:
#     print(bfood[:])
# #buffet_foods[0] = 'turkey'
# buffet_foods = ('turkey','sushi','brocolli','rice','chicken')
# print("\nNew menu.\nThese are the NEW buffet foods:")
# for bfood in buffet_foods:
#     print(bfood[:])