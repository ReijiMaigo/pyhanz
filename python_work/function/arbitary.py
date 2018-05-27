#accept arbitary argument -> list
def print_avenger_lists(*avengers):
    print(avengers)

print_avenger_lists('ironman', 'thor', 'captain america')
print_avenger_lists('black panther', 'vision')

#accept arbitary keyword -> dictionary
def build_profile(first, last, **other):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last

    for key, value in other.items():
        profile[key] = value

    return profile

myprofile = build_profile(first = 'Wei Han', last = 'Ngan', age = '29', company = 'mot')
print(myprofile)
