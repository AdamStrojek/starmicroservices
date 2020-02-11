from starlette.routing import Route

from .resources import CurrentTimeResource, EpochTimeResource

routes = [
    Route('/current_time', endpoint=CurrentTimeResource),
    Route('/epoch_time', endpoint=EpochTimeResource),
]
