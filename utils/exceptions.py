from starlette.exceptions import HTTPException


class APIException(HTTPException):
    pass
