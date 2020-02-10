from starlette.requests import Request

from utils.resources import CreateResource
from utils.auth import get_user_object
from utils.token import create_token


class CreateTokenResource(CreateResource):
    async def create(self, request: Request) -> Any:
        user = await get_user_object()
        data = {
            'user': user
        }
        token = await create_token(data)
        return {
            'token': token
        }
