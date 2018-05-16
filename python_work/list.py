#Print whole list
animals = ["dog", "cat", "bird"]
print(animals)

#Print single item on the list
print(animals[0])

#Print last item on the list
print(animals[-1])
#Print last second item on the list
print(animals[-2])

#Change secnod item name
animals[1] = "duck"
print(animals)

#Append new item into end of list
animals.append("cat")
print(animals)

#Insert new into into second of the list
animals.insert(1, "fish")
print(animals)

#Delete "fish"
del animals[1]
print(animals)

#Pop list
print("pop() without giving index : " + animals.pop())
print("pop(1) : " + animals.pop(1))
animals.remove("bird")
print(animals)

#3.8 Seeing the World
places = ["Malaysia", "Singapore", "Japan", "Korea", "Indonesia"]
print("Exercise 3.8")
print("Print original places list")
print(places)

print('Print "sorted"')
print(sorted(places))

print("Original order in place list")
print(places)

print("Reverse the place list")
places.reverse()
print(places)

print("Back to original order")
places.reverse()
print(places)

print("Sort place list")
places.sort()
print(places)

print("Sort in reverse")
places.sort(reverse = True)
print(places)

print("Length of places list")
print(len(places))
