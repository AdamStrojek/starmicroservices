import abc
from typing import Any, List
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

from utils.permissions import Permission, ResourcePermission
from utils.exceptions import PermissionError
from utils.token import retrive_token

from .responses import APIResponse


class BaseResource(HTTPEndpoint):
    permissions: List[Permission] = []

    async def retrive_data(self, request):
        if 'x-token' in request.headers:
            data = await retrive_token(request.headers['x-token'])
        else:
            user = {}
            data = {
                'user': user
            }
        request.state.data = data

    async def has_permission(self, request):
        for permission in self.permissions:
            if not await permission(request):
                return False
        return True


class RetriveResource(abc.ABC, BaseResource):
    @abc.abstractmethod
    async def retrive(self, request: Request) -> Any:
        pass

    async def get(self, request: Request) -> APIResponse:
        await self.retrive_data(request)

        if not await self.has_permission(request):
            raise PermissionError('this user have no permission to this resource')

        result = await self.retrive(request)
        return APIResponse(result)


class CreateResource(abc.ABC, BaseResource):
    @abc.abstractmethod
    async def create(self, request: Request) -> Any:
        pass

    async def post(self, request: Request) -> APIResponse:
        await self.retrive_data(request)

        if not await self.has_permission(request):
            raise PermissionError('this user have no permission to this resource')

        result = await self.create(request)
        return APIResponse(result, status_code=201)
