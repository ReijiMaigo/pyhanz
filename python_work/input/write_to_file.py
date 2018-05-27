filename = "guests.txt"
loop = True

with open(filename, 'w') as file_object:
    while loop:
        insert_text = raw_input('Insert guest name: ')
        if insert_text.lower() == 'q':
            print('Exit')
            break;
        print('Hello! ' + insert_text)   
        
        file_object.write(insert_text + '\n')
