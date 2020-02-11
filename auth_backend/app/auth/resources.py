from typing import Any
from starlette.requests import Request

from utils.resources import CreateResource, RetriveResource
from utils.auth import get_user_object
from utils.token import create_token, has_permissions
from utils.exceptions import PermissionError
from utils.permissions import HasValidToken


class CreateTokenResource(CreateResource):
    async def create(self, request: Request) -> Any:
        user = await get_user_object()
        data = {
            'user': user,
            'token_valid': True,
        }
        token = await create_token(data)
        return {
            'token': token
        }


class ValidTokenResource(RetriveResource):
    permissions = [HasValidToken()]

    async def retrive(self, request: Request) -> Any:
        resource = request.query_params.get('resource', None)
        if not (await has_permissions(resource, request.state.data['user'])):
            raise PermissionError(f"You have no permissions for {resource}")

        return {}
