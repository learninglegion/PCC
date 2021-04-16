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

#10.2
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
sub_string = ''
for line in lines:
    sub = line.replace('python', 'C')
    sub_string += sub
print(sub_string.rstrip())