from typing import Any
from starlette.responses import UJSONResponse


class APIResponse(UJSONResponse):
    def render(self, content: Any) -> bytes:
        envelope = {
            'data': content,
        }
        return super().render(envelope)
