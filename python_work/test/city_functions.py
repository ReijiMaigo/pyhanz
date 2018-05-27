def city_country_formatted(city, country, population=''):
    """ Accept city and country string and return its format"""
    city_country = city.title() + ', ' + country.title()

    if population:
        city_country +=  ' - population ' + str(population)
    return city_country
