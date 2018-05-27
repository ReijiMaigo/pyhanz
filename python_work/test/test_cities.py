import unittest

from city_functions import city_country_formatted

class CityCountryTestCases(unittest.TestCase):
    """ Unit test main class """
    def test_city_country_formatted(self):
        """ city_country_formatted function test case"""
        self.assertEqual(city_country_formatted("Teluk Intan", "Malaysia"), "Teluk Intan, Malaysia")
    
    def test_city_country_population(self):
        """ city_country_formatted function with population """
        self.assertEqual(
            city_country_formatted("Teluk Intan", "Malaysia", 100000), 
            "Teluk Intan, Malaysia - population 100000")

unittest.main()
