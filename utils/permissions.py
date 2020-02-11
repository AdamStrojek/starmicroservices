from .token import has_permissions

class Permission:
    def __call__(self, request) -> bool:
        return True


class ResourcePermission(Permission):
    def __init__(self, resource):
        self.resource = resource

    async def __call__(self, request) -> bool:
        return await has_permissions(self.resource, request.state.data['user'])
