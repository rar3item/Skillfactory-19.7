from api2 import pf
from settings import valid_email, valid_password, non_valid_email, non_valid_password
import pytest


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_for_valid_user(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_create_pet_simple_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"barsik",
        "animal_type":"cat",
        "age":"5"
    }
    status, result = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert len(result) > 0


def test_delete_pet_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status = pf.delete_pet(auth_key, pet_id='26afef6a-24f4-438f-a7fc-4d05c4007fa3')
    assert status == 200


# тесты по заданию 19.7 ____________________________________________________________

#1 тест на получение ключа для не существующего юзера
def test_get_api_key_for_non_valid_user(email = non_valid_email, password = non_valid_password):
    status, result = pf.get_api_key(email, password)
    assert status != 200

#2 тест на получение списка животных для не существующего фильтра
def test_get_all_pets_for_valid_user_with_incorrect_filter(filter='________'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200

#3 тест на добавление животного с пустыми значениями
def test_create_pet_simple_for_valid_user_without_values():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"",
        "animal_type":"",
        "age":""
    }
    status, result = pf.create_pet_simple(auth_key, params)
    assert status != 200
    return result

#4 тест на удаление животного с пустыми значением
def test_delete_pet_for_valid_user_without_values():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status = pf.delete_pet(auth_key, pet_id='')
    assert status != 200

#5 тест на удаление животного с некорректным значением
def test_delete_pet_for_valid_user_with_incorrect_values():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status = pf.delete_pet(auth_key, pet_id='________________________________________')
    assert status != 200

#6 тест на обновление животного
def test_update_pet_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"felix",
        "animal_type":"britain_cat",
        "age":"2"
    }
    status, result = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert len(result) > 0

#7 тест на обновление животного с пустыми полями
def test_update_pet_for_valid_user_without_form():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"",
        "animal_type":"",
        "age":""
    }
    status, result = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert len(result) > 0

#8 тест на обновление животного с отсутствующим pet_id
def test_update_pet_for_valid_user_without_pet_id():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name": "felix",
        "animal_type": "britain_cat",
        "age": "2"
    }
    status, result = pf.update_pet(auth_key, pet_id='', params=params)
    assert status != 200

#9 тест на обновление животного с кириллическими символами
def test_update_pet_for_valid_user_with_cyrillic_symbol():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"Барсик",
        "animal_type":"Кошка",
        "age":"1"
    }
    status, result = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status == 200
    assert len(result) > 0


#10 тест на обновление животного с отрицательным возрастом
def test_update_pet_for_valid_user_with_negative_age():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"Барсик",
        "animal_type":"Кошка",
        "age":"-1"
    }
    status, result = pf.update_pet(auth_key, pet_id='e4d0652f-9e75-4558-b823-0d0e1e4da0e3', params=params)
    assert status != 200
    assert len(result) > 0

