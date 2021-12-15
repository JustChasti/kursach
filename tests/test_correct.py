from marshmallow.exceptions import ValidationError
import pytest
from utils import correct_test


def test_c_birthday_0():
    user = {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2023",
        "gender": "male",
        'import_id': 1,
        "relatives": [1]
    }
    user_list = [user]
    with pytest.raises(ValidationError) as error:
        correct_test(user, user_list)
    assert "birth_date to high" == error.value.args[0]


def test_c_birthday_1():
    user = {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [1]
    }
    user_list = [user]
    response = correct_test(user, user_list)
    assert response == None


def test_c_relatives_0():
    user = {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [2, 2]
    }
    user2 = {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [1]
    }
    user_list = [user, user2]
    with pytest.raises(ValidationError) as error:
        correct_test(user, user_list)
    assert "no relatives" == error.value.args[0]


def test_c_relatives_1():
    user = {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [2, 3]
    }
    user2 = {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [1]
    }
    user_list = [user, user2]
    with pytest.raises(ValidationError) as error:
        correct_test(user, user_list)
    assert "no relatives" == error.value.args[0]


def test_c_relatives_2():
    user = {
        "citizen_id": 1,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [2]
    }
    user2 = {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "50",
        "apartament": 7,
        "name": "Тимонин Григорий Эдуардович",
        "birth_date": "30.11.2021",
        "gender": "male",
        'import_id': 1,
        "relatives": [1]
    }
    user_list = [user, user2]
    response = correct_test(user, user_list)
    assert response == None


if __name__ == '__main__':
    pytest.main()
