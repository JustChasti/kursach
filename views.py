from marshmallow.exceptions import ValidationError
from pymongo import collection
from db.db import user_collection
import json
from fastapi.responses import JSONResponse
from fastapi import status
from utils import age_percentiles
from loguru import logger
from utils import correct_test, correct_update


def insert_user(data):
    impoted_users = list(user_collection.find({}))
    for i in data["citizens"]:
        if impoted_users:
            last = impoted_users[-1]
            count = last['import_id'] + 1
            i['import_id'] = count
            try:
                correct_test(i, data["citizens"])
            except ValidationError as e:
                logger.exception(e)
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)
            user = user_collection.insert_one(i)
        else:
            count = 1
            i['import_id'] = count
            try:
                correct_test(i, data["citizens"])
            except ValidationError as e:
                logger.exception(e)
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)
            user = user_collection.insert_one(i)
    return {"message": "succes"}


def get_imports_db(import_id):
    users = list(user_collection.find({'import_id': import_id}))
    if not users:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    user_list = []
    for i in users:
        i.pop('_id')
        i.pop('import_id')
        user_list.append(i)
    return json.dumps(user_list, ensure_ascii=False).encode('utf8')


def update_user(import_id, citizen_id, data):
    filter = {'import_id': import_id, 'citizen_id': citizen_id}
    imports = user_collection.find_one(filter=filter)
    if not imports:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    try:
        f = {'import_id': import_id}
        im = user_collection.find(filter=f)
        correct_update(data, list(im))
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST)

    newvalues = {"$set": data}
    imports = user_collection.update_one(filter=filter, update=newvalues)
    if not imports:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    return json.dumps({'status': 'succes'})


def birthdays(import_id):
    users = list(user_collection.find({'import_id': import_id}))
    if not users:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    presents = {
        'jan': 0,
        'feb': 0,
        'mar': 0,
        'apr': 0,
        'may': 0,
        'jun': 0,
        'jul': 0,
        'aug': 0,
        'sep': 0,
        'oct': 0,
        'nov': 0,
        'dec': 0
    }
    month = {
        '01': 'jan',
        '02': 'feb',
        '03': 'mar',
        '04': 'apr',
        '05': 'may',
        '06': 'jun',
        '07': 'jul',
        '08': 'aug',
        '09': 'sep',
        '10': 'oct',
        '11': 'nov',
        '12': 'dec'
    }
    for i in users:
        for j in i['relatives']:
            date = user_collection.find_one({'import_id': import_id, 'citizen_id': j})['birth_date']
            date = date.split('.')[1]
            presents[month[date]] += 1
    return json.dumps(presents)


def percentile(import_id):
    coll = user_collection.find({'import_id': import_id}).sort("town")
    users = list(coll)
    if not users:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    town_list = []
    town = users[0]['town']
    age_list = []
    for i in users:
        if i['town'] == town:
            age_list.append(i['birth_date'])
        else:
            data = {
                'town': town,
                'percentiles': age_percentiles(age_list)
                }
            town_list.append(data)
            town = i['town']
            age_list = [i['birth_date']]
    data = {
        'town': town,
        'percentiles': age_percentiles(age_list)
        }
    town_list.append(data)

    return json.dumps(town_list, ensure_ascii=False).encode('utf8')
