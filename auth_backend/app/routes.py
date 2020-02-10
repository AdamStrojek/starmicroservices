from starlette.routing import Mount, Route

from .auth.routes import routes as auth_routes
from .smoke.routes import routes as smoke_routes


routes = [
    Mount('/api/v1', routes=[
        Mount('/auth', routes=auth_routes),
        Mount('/smoke', routes=smoke_routes),
    ]),
]
