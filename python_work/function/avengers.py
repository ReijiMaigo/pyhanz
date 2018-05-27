def show_avengers(avengers):
    for avenger in avengers:
        print(avenger)

def make_great(avengers):
    for i in range(len(avengers)):
        avengers[i] = "the great " + avengers[i]
    return avengers

avengers = ['ironman', 'thor', 'vision', 'black panther']

new_list = make_great(avengers[:])
show_avengers(avengers)
show_avengers(new_list)
