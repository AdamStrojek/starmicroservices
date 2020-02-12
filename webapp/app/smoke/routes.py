from starlette.routing import Route

from .resources import SmokeResource


routes = [
    Route('/', endpoint=SmokeResource),
]
