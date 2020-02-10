import abc
from typing import Any
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

from .responses import APIResponse


class BaseResource(HTTPEndpoint):
    pass


class RetriveResource(abc.ABC, BaseResource):
    @abc.abstractmethod
    async def retrive(self, request: Request) -> Any:
        pass

    async def get(self, request: Request) -> APIResponse:
        result = await self.retrive(request)
        return APIResponse(result)
