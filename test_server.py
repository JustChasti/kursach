import requests
import json
from tests.generator import generate_dataset


url = 'http://194.58.122.212:8000/'
id = 2


def test_imports():
    data = {
        "citizens": generate_dataset(10)
    }
    response = requests.post(f"{url}imports", data=json.dumps(data))
    print(response)
    print(response.json())


def test_import_id():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}")
    print(response)
    print(response.json())


def test_birthdays():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}/citizens/birthdays")
    print(response)
    print(response.json())


def test_percentile():
    import_id = id
    response = requests.get(f"{url}imports/{import_id}/towns/stat/percentile/age")
    print(response)
    print(response.json())


# test_imports()
# test_import_id()
# test_birthdays()
# test_percentile()
