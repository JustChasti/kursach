from fastapi import Request, FastAPI
from fastapi.encoders import jsonable_encoder
from loguru import logger
from pymongo import response

from views import insert_user, get_imports_db, update_user
from views import birthdays, percentile


app = FastAPI()
logger.add("test.log", rotation="100 MB")


@app.post("/imports")
# добавить проверку корректности данных и вернуть 400 если они некорректные
async def imports(request: Request):
    try:
        response = insert_user(await request.json())
        return response
    except Exception as e:
        logger.exception(e)
        return {"message": "db insert error"}


@app.get("/imports/{import_id}")
async def get_imports(import_id: int):
    try:
        result = get_imports_db(import_id)
        return result
    except Exception as e:
        logger.exception(e)
        return {"message": "import error"}


@app.patch("/imports/{import_id}/citizens/{citizen_id}")
# проверить данные, если не ок, то 400, если челобаса нет, то 404
async def change_person(import_id: int, citizen_id: int, request: Request):
    response = update_user(import_id, citizen_id, await request.json())
    return response


@app.get("/imports/{import_id}/citizens/birthdays")
async def count_relatives(import_id: int):
    try:
        result = birthdays(import_id)
        return result
    except Exception as e:
        logger.exception(e)
        return {"message": "birthdays error"}


@app.get("/imports/{import_id}/towns/stat/percentile/age")
async def get_percentile(import_id: int):
    # percentile - например есть 10 берем значение перцентель 30 и сортируем массив по возрастанию, значит 3-й элемент массива - 30 перцентель percentel = array[p * N / 100]
    try:
        result = percentile(import_id)
        return result
    except Exception as e:
        logger.exception(e)
        return {"message": "percentile error"}
