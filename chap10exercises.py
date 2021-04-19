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