from .remote import call_remote


class Permission:
    message = "User has no permission for this resource"

    def __call__(self, request) -> bool:
        return True


class ResourcePermission(Permission):
    def __init__(self, resource):
        self.resource = resource

    async def __call__(self, request) -> bool:
        status, data = await call_remote('get', 'auth', 'valid', request.headers, resource=self.resource)
        return status < 400


class HasValidToken(Permission):
    message = "Invalid token"

    async def __call__(self, request) -> bool:
        return request.state.data.get('token_valid', False)
