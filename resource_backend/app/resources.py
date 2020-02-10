from typing import Any
from datetime import datetime
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request

from utils.responses import APIResponse


class CurrentTimeResource(HTTPEndpoint):
    async def get(self, request: Request) -> APIResponse:
        result = {
            'current_time': datetime.now().isoformat(),
        }
        return APIResponse(result)


class EpochTimeResource(HTTPEndpoint):
    async def get(self, request: Request) -> APIResponse:
        result = {
            'epoch_time': int(datetime.now().timestamp()),
        }
        return APIResponse(result)
