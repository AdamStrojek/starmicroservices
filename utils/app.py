from starlette.applications import Starlette as Application


def setup_app(settings, routes, middleware) -> Application:
    middleware = []
    app = Application(debug=settings.DEBUG, routes=routes, middleware=middleware)
    return app
