from faker import Faker

fake = Faker()

class Register:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return {'username': username, 'password': password}
