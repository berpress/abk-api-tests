from fixtures.register.api import Register


class App:
    def __init__(self, url: str):
        self.url = url
        self.register = Register(self)