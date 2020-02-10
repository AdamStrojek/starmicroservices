import datetime
import jwt
from typing import Union
import ujson

from app import settings
from .exceptions import TokenExpired

async def create_token(data, expiration_time: int = 5):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_time),
        'data': data
    }
    result = jwt.encode(payload, str(settings.JWT_SECRET), algorithm='HS256')
    return result


async def retrive_token(token: Union[bytes, str]):
    try:
        result = jwt.decode(token, str(settings.JWT_SECRET), algorithm='HS256')
    except jwt.ExpiredSignatureError as exp:
        raise TokenExpired("Token expired")
    data = result.get('data', None)
    return data
