avenger1 = {
    'name' : 'Tony',
    'superhero' : 'Ironman'
}
avenger2 = {
    'name' : 'Stave',
    'superhero' : 'Captain America'
}
avenger3 = {
    'name' : 'Burce',
    'superhero' : 'Hulk'
}
avenger4 = {
    'name' : 'Peter',
    'superhero' : 'Spiderman'
}
avenger5 = {
    'name' : 'Natasha',
    'superhero' : 'Black Widow'
}

avengers = [avenger1, avenger2, avenger3, avenger4, avenger5]

for avenger in avengers:
    for key, value in avenger.items():
        print(key + " : " + value)

