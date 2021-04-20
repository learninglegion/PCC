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

#10.10
filename = 'huckfinn.txt'

print("Let's search for words in a book.")
searchword = input("Give me a word to search for: ")
searchword_count = 0

with open(filename, encoding='utf-8') as f:
    #contents = f.read()
    #words = contents.split()
    #num_words = len(words)
    #print(f"The file {filename} has {num_words} words in it.")
    for line in f:
        searchword_count += line.lower().count(f'{searchword}')
print(f"The file {filename} has {searchword_count} '{searchword}'s in it.")