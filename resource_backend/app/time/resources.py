from typing import Any
from datetime import datetime
from starlette.requests import Request

from utils.resources import RetriveResource
from utils.responses import APIResponse


class CurrentTimeResource(RetriveResource):
    async def retrive(self, request: Request) -> Any:
        result = {
            'current_time': datetime.now().isoformat(),
        }
        return result


class EpochTimeResource(RetriveResource):
    async def retrive(self, request: Request) -> Any:
        result = {
            'epoch_time': int(datetime.now().timestamp()),
        }
        return result
