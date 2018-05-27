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

restaurant1 = Restaurant('E&O', 'western')
restaurant2 = Restaurant('Aji', 'japanese')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(13)
restaurant1.increment_number_served(100)
restaurant1.print_number_served()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.set_number_served(45)
restaurant2.increment_number_served(100)
restaurant2.print_number_served()
