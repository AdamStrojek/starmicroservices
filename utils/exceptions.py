from starlette.exceptions import HTTPException


class APIException(HTTPException):
    pass


class TokenExpired(APIException):
    status_code = 401

    def __init__(self, detail = None):
        super().__init__(self.status_code, detail)
