import requests




# Что нужно исправить/добавить/сделать
# 1. PO для API тестов (убрать requests) +
# 2. URL вынести в конфиг +
# 3. Добавить faker (модель) +
# 4. Валидация респонса -
# 5. Документация -
from fixtures.register.model import Register


class TestRegister:
    def test_valid_register_2(self):
        url = 'https://stores-tests-api.herokuapp.com/register'
        r = requests.post(url, data={'username': 'test2211211', 'password': 'Password11'})
        assert r.status_code == 201
        assert r.json().get('message') == 'User created successfully.'
        assert r.json().get('uuid') is not None
        assert isinstance(r.json().get('uuid'), int)
        print(f'Status code is {r.status_code}, url: {r.url}, response: {r.text}')

    def test_valid_register(self, app):
        """
        1. Try to register new user
        2. Check status code is 201
        3. Check response
        """
        data = Register.random()
        res = app.register.new_register(data=data)
        assert res.status_code == 201
        assert res.json().get('message') == 'User created successfully.'
        assert res.json().get('message').get('message')[0].get('dkkdk') == 'User created successfully.'

