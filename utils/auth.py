

async def get_user_object(user=None):
    return {
        'permissions': await get_user_permissions(user),
    }


async def get_user_permissions(user=None):
    return ['smoke']
