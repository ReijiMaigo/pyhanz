royalCards = {
    'Hog Rider' : {
        'damage' : 384,
        'hitpoint' : 2048,
        'dps' : 240,
    },

    'Archers' : {
        'damage' : 126,
        'hitpoint' : 370,
        'dps' : 105,
    },

    'Giants' : {
        'damage' : 279,
        'hitpoint' : 4427,
        'dps' : 186,
    },
}

for card, characteristics in royalCards.items():
    print(card)
    print("damage : " + str(characteristics['damage'])) 
    print("hitpoint: " + str(characteristics['hitpoint'])) 
    print("dps: " + str(characteristics['dps'])) 
