#5-3 ~ 5-5 Alien Colors
print("5-3 ~ 5-5")
alien_color = "yellow"

if alien_color == "green":
    point = 5
elif alien_color == "yellow":
    point = 10
elif alien_color == "red":
    point = 15
else:
    point = 10

print("it is " + alien_color + "! " + str(point) + " points!!!\n\n")


#5-6 Stages of Life
age = 54

if age < 2:
    stage = "baby"
elif age >= 2 and age < 4:
    stage = "toddler"
elif age >= 4 and age < 13:
    stage = "kid"
elif age >= 13 and age < 20:
    stage = "teenager"
elif age >= 20 and age < 65:
    stage = "adult"
else:
    stage = "elder"

print("Stage = " + stage + "\n\n")

#5-8 Hello Admin
#names = ["WeiHan", "Adam", "Thor", "Admin", "Tony"]
names = []

if names:
    for name in names:
        if name.lower() == "admin":
            print("Hello admin, would you like to see the status report?")
        else:
            print("Hello " + name + ", thank you for logging in again.")
else:
    print("We need to find new user.\n\n")

new_users = ["Ironman", "Thor", "Captain", "Spidey", "Winter"]
current_users = ["BlackW", "Witch", "THor", "SpidEy", "Vision"]

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print("You need to enter a new username " + new_user + "\n\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ordinal_numbers = []

for number in numbers:
    if number == 1:
        ordinal_numbers.append(str(number) + "st")
    elif number == 2:
        ordinal_numbers.append(str(number) + "nd")
    elif number == 3:
        ordinal_numbers.append(str(number) + "rd")
    else:
        ordinal_numbers.append(str(number) + "th")

print(ordinal_numbers)


