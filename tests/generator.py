import random
import string


town_list = ['Москва', 'Санкт-Петербург', 'Нижний Новгород', 'Владимир']

gender_list = ['male', 'female']


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_list(count):
    rel_list = []
    for i in range(random.randint(0, count-1)):
        data = random.randint(1, count-1)
        if data not in rel_list:
            rel_list.append(data)
    return rel_list


def generate_date(num):
    d = random.randint(1, num)
    d = str(d)
    if len(d) < 2:
        return f'0{d}'
    else:
        return d


def generate_dataset(count):
    user_list = []
    for i in range(count):
        user = {
            "citizen_id": i,
            "town": town_list[random.randint(0, 3)],
            "street": randomword(12),
            "building": randomword(4),
            "apartament": random.randint(0, 100),
            "name": randomword(20),
            "birth_date": f"{generate_date(28)}.{generate_date(12)}.{random.randint(1900,2021)}",
            "gender": gender_list[random.randint(0, 1)],
            "relatives": generate_list(count)
        }
        user_list.append(user)
    return user_list
