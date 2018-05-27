#Simple function return
def city_country(city, country):
    """Return <city>, <country> format"""
    return city + ', ' + country

print(city_country('Teluk Intan', 'Malaysia'))
print(city_country('Taipei', 'Taiwan'))
print(city_country('Shanghai', 'China'))

print('\n\n')

#function return dictionary
def city_country_dict(city, country):
    """Return in dictionary format"""
    return {'city': city, 'country': country}

print(city_country_dict('Teluk Intan', 'Malaysia'))
print(city_country_dict('Taipei', 'Taiwan'))
print(city_country_dict('Shanghai', 'China'))

print('\n\n')

#Add input
while True:
    print('\nPlease insert a city')
    print('(press "q" to quit)')
    city= raw_input('city: ')

    if city == 'q':
        break;

    print('\nPlease insert a country')
    print('(press "q" to quit)')
    country = raw_input('Country: ')

    if country == 'q':
        break;

    print(city_country_dict(city, country))

