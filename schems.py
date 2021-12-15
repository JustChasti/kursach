from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    citizen_id = fields.Int(required=True)
    town = fields.String(required=True)
    street = fields.String(required=True)
    building = fields.String(required=True)
    apartament = fields.Int(required=True)
    name = fields.String(required=True)
    birth_date = fields.Date(required=True, format='%d.%m.%Y')
    gender = fields.String(required=True)
    relatives = fields.List(fields.Int(), required=True)
    import_id = fields.Int(required=True)


def test():
    user = {
        "citizen_id": 3,
        "town": "Керчь",
        "street": "Иосифа Бродского",
        "building": "2",
        "apartament": 11,
        "name": "Романова Мария Леонидовна",
        "birth_date": "23.11.1986",
        "gender": "female",
        "relatives": [1]
    }

    schema = UserSchema()
    user = schema.load(user)
