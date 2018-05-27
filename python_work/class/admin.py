class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('First name = ' + self.first_name +
                '\nLast name = ' + self.last_name)

    def greet_user(self):
        print('Hello, ' + self.first_name)


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Privileges : ')
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


my_admin = Admin('Wei Han', 'Ngan')
my_admin.privileges.show_privileges()
