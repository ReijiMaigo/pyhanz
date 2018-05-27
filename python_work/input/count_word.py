books = ['The little black princess.txt', 'The subsitude millionaire.txt']

search = raw_input('Insert the text you which to count: ')

for book in books:
    with open(book) as file_object:
        content = file_object.readlines()
    
    count = 0
    total_word = 0
    for line in content:
        count += line.lower().count(search)
        total_word += len(line.split())
    
    print(book + ' contains ' + str(count) + ' ' + '"' + search + '" words')
    print(total_word)
