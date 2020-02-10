from starlette.routing import Route

from .resources import CreateTokenResource


routes = [
    Route('/create', endpoint=CreateTokenResource),
]
