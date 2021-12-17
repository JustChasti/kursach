import pytest
import requests
import json
from generator import generate_dataset


url = 'http://127.0.0.1:8000/'
id = 1


def test_imports():
    data = {
        "citizens": generate_dataset(10)
    }
    response = requests.post(f"{url}imports", data=json.dumps(data)).json()
    assert response == {"message": "succes"}


def test_import_id():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}")
    assert str(response) == "<Response [200]>"


def test_birthdays():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}/citizens/birthdays")
    assert str(response) == "<Response [200]>"


def test_percentile():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}/towns/stat/percentile/age")
    assert str(response) == "<Response [200]>"


if __name__ == '__main__':
    pytest.main()
