import json

number = raw_input('What is your favourite number? ')

filename = 'number.txt'

#Store to file
with open(filename, 'w') as file_object:
    json.dump(str(number), file_object)

#Read from file
with open(filename, 'r') as file_object:
    print(json.load(file_object))
