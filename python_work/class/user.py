class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('First name = ' + self.first_name +
                '\nLast name = ' + self.last_name)

    def greet_user(self):
        print('Hello, ' + self.first_name)

myself = User('Wei Han', 'Ngan')
myself.describe_user()
myself.greet_user()
