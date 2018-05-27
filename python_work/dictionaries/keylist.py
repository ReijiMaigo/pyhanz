royalCards = {
    'globins' : ['globin', 'globin gang', 'spear globin', 'globin hut'],
    'knights' : ['knight', 'dark knight', 'mega knight'],
    'babarians' : ['babarian', 'babarian hut', 'babarian barrel'],
}

for catagory, cards in royalCards.items():
    print("\n" + catagory + " : ")
    for card in cards:
        print(card)
