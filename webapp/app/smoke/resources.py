from typing import Any
from datetime import datetime
from starlette.requests import Request

from utils.resources import RetriveResource
from utils.responses import APIResponse


class SmokeResource(RetriveResource):
    """
    This resource is just for smoke testing. It will always return 200 OK,
    so it can be used to deterin does server started correctly during CI/CD
    """

    async def retrive(self, request: Request) -> Any:
        result = {
            'status': 'OK',
        }
        return result
