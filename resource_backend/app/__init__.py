from starlette.applications import Starlette as Application

from . import settings
from .routes import routes


def setup_app() -> Application:
    middleware = []
    app = Application(debug=settings.DEBUG, routes=routes, middleware=middleware)
    return app


app = setup_app()
