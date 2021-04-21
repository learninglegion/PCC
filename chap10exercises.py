#10.1
# with open('learning_python.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# filename = 'learning_python.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.strip())

# with open(filename) as file_object:
#     lines = file_object.readlines()
# text_string = ''
# for line in lines:
#      text_string += line
# print(text_string.rstrip())
#
##10.2
#filename = 'learning_python.txt'
#
#with open(filename) as file_object:
#    lines = file_object.readlines()
#sub_string = ''
#for line in lines:
#    sub = line.replace('python', 'C')
#    sub_string += sub
#print(sub_string.rstrip())

#10.3
#filename = 'guest.txt'
#
#with open(filename, 'w') as file_object:
#    print("Please provide your name for the guestbook.")
#    file_object.write(input("Your name: "))

##10.4
#filename = 'guest_book.txt'
#finished = False
#
#while finished == False:
#    with open(filename, 'a') as file_object:
#        name = input("Please provide your names for the guestbook (type 'q' when finished): ")
#        if name == 'q':
#            finished = True
#            break
#        print(f"Thanks for coming, {name}! Welcome!")
#        name = name + '\n'
#        file_object.write(name)

##10.5.
#brent.windstreamhosting.bizme = 'programming_poll.txt'
#finished = False
#
#while finished == False:
#    with open(filename, 'a') as file_object:
#        name = input("Please enter your name for the poll ('q' if finished): ")
#        if name == 'q':
#            finished = True
#            break
#        reason = input("Why do you like programming: ")
#        file_object.write(f"{name} answered '{reason}'.\n")

##10.6 and 10.7
#print("Give me two numbers and I'll add them.")
#print("Type 'q' to quit.")
#while True:
#    first_number = input("First number: ")
#    if first_number == 'q':
#        break
#    second_number = input("Second number: ")
#    if second_number == 'q':
#        break
#    try:
#        print(int(first_number) + int(second_number))
#    except ValueError:
#        print("Numbers only please.")

##10.8 and 10.9
#filenames = ['cats.txt', 'dogs.txt']
#
#for filename in filenames:
#    try:
#        with open(filename) as f:
#            for line in f:
#                print(line.title().rstrip())
#    except FileNotFoundError:
#        #print(f"I could not find {filename}.")
#        pass

##10.10
#filename = 'huckfinn.txt'
#
#print("Let's search for words in a book.")
#searchword = input("Give me a word to search for: ")
#searchword_count = 0
#
#with open(filename, encoding='utf-8') as f:
#    #contents = f.read()
#    #words = contents.split()
#    #num_words = len(words)
#    #print(f"The file {filename} has {num_words} words in it.")
#    for line in f:
#        searchword_count += line.lower().count(f'{searchword}')
#print(f"The file {filename} has {searchword_count} '{searchword}'s in it.")

#10.11 and 10.12
#import json
#
#def get_stored_number():
#    """Say favorite number"""
#    filename = 'favnum.json'
#    try:
#        with open(filename) as f:
#            favnum = json.load(f)
#    except FileNotFoundError:
#        return None
#    else:
#        return favnum
#
#def get_new_number():
#    """Ask for favorite number"""
#    filename = 'favnum.json'
#    favnum = input("What is your favorite number? ")
#    with open(filename, 'w') as f:
#        json.dump(favnum, f)
#    return favnum
#
#def favorite_number():
#    """Ask for favorite number if we don't know it."""
#    favnum = get_stored_number()
#    if favnum:
#        print(f"I know your favorite number, it's {favnum}!")
#    else:
#        favnum = get_new_number()
#
#favorite_number()

#10.13
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

def check_user():
    username = get_stored_username()
    answer = ''
    print(f"Is {username} your username?")
    while answer != 'y' or answer != 'n':
        answer = input("Type 'y' or 'n' to answer: ")
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            print("Answer 'y' or 'n' please.")

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        if check_user() == True:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username.title()}!")

greet_user()