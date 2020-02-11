from starlette.exceptions import HTTPException


class APIException(HTTPException):
    status_code = 400

    def __init__(self, detail = None):
        super().__init__(self.status_code, detail)


class TokenExpired(APIException):
    status_code = 401


class PermissionError(APIException):
    status_code = 403
