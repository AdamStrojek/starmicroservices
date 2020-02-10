from utils.app import setup_app

from . import settings
from .routes import routes
from .middlewares import middlewares


app = setup_app(settings, routes, middlewares)
