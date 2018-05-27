def get_number(index):
    """ Get number function """
    return raw_input('Insert your number ' + str(index) + ' : ')

exit = True
while exit:
    sum_number = 0

    for index in range(0, 2):
        try:
            sum_number += int(get_number(index)) 
        except ValueError:
            print('Exit')
            exit = False 
            break
    
    if index == 1:
        print('Sum = ' + str(sum_number))
        sum_number = 0;
        index = 0;
