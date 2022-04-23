from fixtures.register.api import Register
from fixtures.requests import Client


class App:
    def __init__(self, url: str):
        self.client = Client
        self.url = url
        self.register = Register(self)