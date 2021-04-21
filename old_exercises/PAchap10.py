# #pi_string
# filename = 'pi_million_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# # print(f"{pi_string[:52]}...")
# # print(len(pi_string))

# #birthday in pi?
# birthday = input("Enter your birthday in the format mmddyyyy: ")
# if birthday in pi_string:
#     print ("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")


##write_message
#filename = 'programming.txt'
#
##with open(filename, 'w') as file_object:
##    file_object.write("I love programming.\n")
##    file_object.write("I love creating new games.\n")
#
#with open(filename, 'a') as file_object:
#    file_object.write("I also love finding meaning in large datasets.\n")
#    file_object.write("I love creating apps that can run in a browser.\n")

##division_calculator
#try:
#    print(5/0)
#except ZeroDivisionError:
#    print("You can't divide by zero!")
#print("Give me twho numbers and I'll divide them.")
#print("Type 'q' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number) / int(second_number)
#    except ZeroDivisionError:
#        print("You can't divide by zero!")
#    else:
#        print(answer)


##alice
##filename = 'alice.txt'
#filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
#
#def count_words(filename):
#    """Count the approximate number of words in a file"""
#    try:
#        with open(filename, encoding='utf-8') as f:
#            contents = f.read()
#    except FileNotFoundError:
#        #print(f"Sorry, the file {filename} does not exist.")
#        pass
#    else:
#        words = contents.split()
#        num_words = len(words)
#        print(f"The file {filename} has {num_words} words in it.")
#
#for filename in filenames:
#    count_words(filename)

#number_writer/reader
#
#import json
#
#numbers = [2, 3, 5, 7, 11, 13]
#filename = 'numbers.json'
#with open(filename, 'w') as f:
#    json.dump(numbers, f)
#
#filename = 'numbers.json'
#with open(filename) as f:
#    numbers = json.load(f)
#print(numbers)

##remember_me/greet user
#import json
##
##Load the username if it has been stored previously
##otherwise, prompt for username and store it.
#filename = 'username.json'
#try:
#    with open(filename) as f:
#        username = json.load(f)
#except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename, 'w') as f:
#        json.dump(username, f)
#        print(f"We'll remember you when you come back, {username}!")
#else:
#    print(f"Welcome back, {username}!")
#

#remember_me/greet user REFACTORED
import json

def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    filename = 'username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()