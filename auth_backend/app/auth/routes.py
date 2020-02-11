from starlette.routing import Route

from .resources import CreateTokenResource, ValidTokenResource


routes = [
    Route('/create', endpoint=CreateTokenResource),
    Route('/valid', endpoint=ValidTokenResource),
]
