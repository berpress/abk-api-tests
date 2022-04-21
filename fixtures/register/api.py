import requests


class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = '/register'

    def new_register(self, data: dict):
        res = requests.post(f"{self.app.url}{self.POST_REGISTER}",
                      json=data)
        return res

    def delete_register(self, data: dict):
        res = requests.delete(f"{self.app.url}{self.POST_REGISTER}",
                      json=data)
        return res