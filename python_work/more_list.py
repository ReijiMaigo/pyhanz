#4-1
#list pizza
pizzas = ["vege", "beef", "seafoot", "fish"]

#Print it using for loot
for pizza in pizzas:
    print(pizza)
    print("I like " + pizza + " pizza.")

print("I really like pizza")


#4-3
print("####################################")
#Print 1 to 20
for number in range(1, 21):
    print(number)

#4.4
print("####################################")
#Print one miliion number
numbers = [range(1, 1000000)]

#4.5
print("####################################")
#Print max, min, sum
digits = []
for value in range(1, 1000000):
    digits.append(value)
print(max(digits))
print(min(digits))
print(sum(digits))


#4.6
print("####################################")
#Print odd number from 1 - 20
digits = [range(1, 21, 2)]
print(digits)

#4.7
print("####################################")
#Print multpile of 3 from 3 to 30
digits = [range(3, 31, 3)]
for digit in digits:
    print(digit)

#4.8
print("####################################")
digits = []
for number in range(1, 11):
    digits.append(number ** 3)
    print(digits[number - 1])
    
#4.9
print("####################################")
#List Comprehensions
digits = [ number ** 3 for number in range(1, 11)]
print(digits)

#4.10
print("####################################")
#Print using slice
print("The first 3 items are :")
print(digits[:3])
print("Items 4 to 6 are :")
print(digits[4:7])
print("The last 3 items are :")
print(digits[-3:])

#4.11
print("####################################")
#Copy list
friend_pizzas = pizzas[:]
pizzas.append("More cheese")
friend_pizzas.append("Less cheese")
print(pizzas)
print(friend_pizzas)

#4-13
print("####################################")
#tuple
tuple_digits = (19, 123, 4, 5)
for tuple_digit in tuple_digits:
    print(tuple_digit)
