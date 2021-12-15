import requests
import json


def test_imports():
    """
    data = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к1",
                "apartament": 7,
                "name": "Иванов Иван Иванович",
                "birth_date": "26.12.1986",
                "gender": "male",
                "relatives": [2]
            },
            {
                "citizen_id": 2,
                "town": "Москва",
                "street": "Льва Толстого",
                "building": "16к1",
                "apartament": 7,
                "name": "Иванов Сергей Иванович",
                "birth_date": "1.04.1997",
                "gender": "male",
                "relatives": [1]
            },
            {
                "citizen_id": 3,
                "town": "Керчь",
                "street": "Иосифа Бродского",
                "building": "2",
                "apartament": 11,
                "name": "Романова Мария Леонидовна",
                "birth_date": "23.11.1986",
                "gender": "female",
                "relatives": []
            },
            {
                "citizen_id": 4,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Григорий Эдуардович",
                "birth_date": "30.11.2001",
                "gender": "male",
                "relatives": [2, 3]
            },
            {
                "citizen_id": 5,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Эдуард Евгеньевич",
                "birth_date": "18.09.1966",
                "gender": "male",
                "relatives": [1, 3]
            },
            {
                "citizen_id": 6,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Государева Ольга Дмитриевна",
                "birth_date": "12.04.1971",
                "gender": "female",
                "relatives": [1, 2]
            }
        ]
    }
    """

    """
    data = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Григорий Эдуардович",
                "birth_date": "30.11.2001",
                "gender": "male",
                "relatives": [2, 3]
            },
            {
                "citizen_id": 2,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Эдуард Евгеньевич",
                "birth_date": "18.09.1966",
                "gender": "male",
                "relatives": [1, 3]
            },
            {
                "citizen_id": 3,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Государева Ольга Дмитриевна",
                "birth_date": "12.04.1971",
                "gender": "female",
                "relatives": [1, 2]
            }
        ]
    }
    """

    data = {
        "citizens": [
            {
                "citizen_id": 1,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Григорий Эдуардович",
                "birth_date": "30.11.2020",
                "gender": "male",
                "relatives": [2]
            },
            {
                "citizen_id": 2,
                "town": "Ковров",
                "street": "Льва Толстого",
                "building": "50",
                "apartament": 7,
                "name": "Тимонин Эдуард Евгеньевич",
                "birth_date": "18.09.1966",
                "gender": "male",
                "relatives": [1]
            }
        ]
    }

    print(requests.post("http://127.0.0.1:8000/imports", data=json.dumps(data)).json())


def test_import_id(import_id):
    response = requests.get(f"http://127.0.0.1:8000/imports/{import_id}")
    print(response)
    print(response.json())


def test_change(import_id, citizen_id):
    data = {
        "relatives": [2, 2]
    }
    response = requests.patch(f"http://127.0.0.1:8000/imports/{import_id}/citizens/{citizen_id}", data=json.dumps(data))
    print(response)
    print(response.json())


def test_birthdays(import_id):
    response = requests.get(f"http://127.0.0.1:8000/imports/{import_id}/citizens/birthdays")
    print(response)
    print(response.json())


def test_percentile(import_id):
    response = requests.get(f"http://127.0.0.1:8000/imports/{import_id}/towns/stat/percentile/age")
    print(response)
    print(response.json())


# test_change(1, 1)
test_import_id(1)
