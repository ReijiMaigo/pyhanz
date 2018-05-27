class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ' is a ' + self.cuisine + ' restaurant.')

    def open_restaurant(self):
        print(self.name + ' is open!')

    def print_number_served(self):
        print('Number served : ' + str(self.number_served))

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, number_increase):
        self.number_served += number_increase


class IceCreamStand(Restaurant):
    """
    Inherit from Restaurant class
    """

    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)

    def print_flavors(self):
        print('Flavors : ' + self.flavors)

my_ice_cream = IceCreamStand('iceiceice', 'dessert', 'apple')
my_ice_cream.describe_restaurant();
my_ice_cream.open_restaurant();
my_ice_cream.print_number_served();
my_ice_cream.print_flavors();
