import numpy as np
from datetime import datetime, timedelta
from time import mktime
from schems import UserSchema
from marshmallow.exceptions import ValidationError


def age_percentiles(dates):
    d_dates = []
    for i in dates:
        d_dates.append((datetime.now().date() - datetime.strptime(i, '%d.%m.%Y').date()).days)
    array = np.array(d_dates)
    return {
        '50': (datetime.now().date() - timedelta(days=int(np.percentile(array, 50)))).strftime('%d.%m.%Y'),
        '75': (datetime.now().date() - timedelta(days=int(np.percentile(array, 75)))).strftime('%d.%m.%Y'),
        '99': (datetime.now().date() - timedelta(days=int(np.percentile(array, 99)))).strftime('%d.%m.%Y'),
        }


def correct_test(element, array):
    schema = UserSchema()
    su = schema.load(element)
    if su["birth_date"] > datetime.now().date():
        raise ValidationError(message="birth_date to high")
    try:
        set_arr = set(su["relatives"])
        if len(su["relatives"]) != len(set_arr):
            raise ValidationError(message="no relatives")
        for i in su["relatives"]:
            if array[i-1]["citizen_id"] != su["citizen_id"]:
                pass
            else:
                pass
                # raise ValidationError(message="no relatives")
    except Exception as e:
        raise ValidationError(message="no relatives")


def correct_update(upd, array):
    res_a = False
    res_b = False
    try:
        birth_date = upd['birth_date']
        res_a = True
    except Exception as e:
        pass
    try:
        relatives = upd['relatives']
        res_b = True
    except Exception as e:
        pass
    if res_a:
        try:
            data = datetime.strptime(birth_date, '%d.%m.%Y')
            if data.date() > datetime.now().date():
                raise ValidationError(message="birth_date error")
        except Exception as e:
            raise ValidationError(message="birth_date error")
    if res_b:
        set_arr = set(relatives)
        if len(relatives) != len(set_arr):
            raise ValidationError(message="no relatives")
