from typing import Any
from datetime import datetime
from starlette.requests import Request

from utils.resources import RetriveResource
from utils.remote import call_remote


class CurrentTimeResource(RetriveResource):
    async def retrive(self, request: Request) -> Any:
        status, data = await call_remote('post', 'auth', 'create', {})

        token = data['data']['token']

        status, data = await call_remote('get', 'resource', 'current_time', {'x-token': token})

        return data['data']


class EpochTimeResource(RetriveResource):
    async def retrive(self, request: Request) -> Any:
        status, data = await call_remote('post', 'auth', 'create', {})

        token = data['data']['token']

        status, data = await call_remote('get', 'resource', 'epoch_time', {'x-token': token})

        return data['data']
