from starlette.routing import Mount, Route

from .smoke.routes import routes as smoke_routes


routes = [
    Mount('/api/v1', routes=[
        Mount('/smoke', routes=smoke_routes),
    ]),
]
