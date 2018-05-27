#6-1 Person
myself = {"first_name" : "Wei Han", "last_name" : "Ngan", "age" : 29, "city" : "Teluk Intan"}
mygf = {"first_name" : "Poh Ling", "last_name" : "Gan", "age" : 28, "city" : "Muar"}
people = [myself, mygf]
print(people)

#print(myself)
print("\n\n")

#6-2 Favourite Numbers
favourite_numbers = {"ironman" : 1, "captain" : 2, "hulk" : 3, "thor" : 4, "vision" : 5}
print("Ironman : " + str(favourite_numbers["ironman"]))
print("Caption America : " + str(favourite_numbers['captain']))
print("Hulk : " + str(favourite_numbers['hulk']))
print("Thor : " + str(favourite_numbers['thor']))
print("Vision : " + str(favourite_numbers['vision']))
print("\n\n")

for name, number in favourite_numbers.items():
    print(name + " : " + str(number))

favourite_numbers = {'witch' : 5}
favourite_numbers = {'groot' : 6}
favourite_numbers = {'rocket' : 7}
favourite_numbers = {'starlord' : 8}
favourite_numbers = {'tharnos' : 9}

print("\n\n")
for name, number in favourite_numbers.items():
    print(name + " : " + str(number))


