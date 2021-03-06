import pytest
import requests




# Что нужно исправить/добавить/сделать
# 1. PO для API тестов (убрать requests) +
# 2. URL вынести в конфиг +
# 3. Добавить faker (модель) +
# 4. Валидация респонса +
# 5. Документация -
from fixtures.register.model import RegisterModel, RegisterUserResponse, \
    RegisterUserInvalidResponse


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
        data = RegisterModel.random()
        res = app.register.new_register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == 'User created successfully.'


    @pytest.mark.parametrize('field', [
        'username', 'password'
    ])
    def test_register_empty_field(self, app, field):
        """
        1. Try to register new user, one field is empty
        2. Check status code is 400
        3. Check response
        """
        data = RegisterModel.random()
        setattr(data, field, None)
        res = app.register.new_register(data=data, type_response=RegisterUserInvalidResponse)
        assert res.status_code == 400
        assert res.data.message == 'Username and password are required fields'

    def test_valid_double_register(self, app):
        """
        1. Try to double register new user
        2. Check status code is 400
        3. Check response
        """
        data = RegisterModel.random()
        res_first = app.register.new_register(data=data, type_response=RegisterUserResponse)
        assert res_first.status_code == 201
        assert res_first.data.message == 'User created successfully.'
        res_second = app.register.new_register(data=data, type_response=RegisterUserInvalidResponse)
        assert res_second.status_code == 400
        assert res_second.data.message == 'A user with that username already exists'

    @pytest.mark.skip(reason='Need fix back')
    def test_short_password_register(self, app, password='124'):
        """
        1. Try to register new user
        2. Check status code is 400
        3. Check response
        """
        data = RegisterModel.random()
        setattr(data, 'password', password)
        res = app.register.new_register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201
        assert res.data.message == 'User created successfully.'
