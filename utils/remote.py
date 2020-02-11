import aiohttp


remote_service_map = {
    "auth": "auth:5040",
    'resource': 'resource:5050'
}


async def call_remote(service, endpoint, headers: dict, version='v1', **data):
    url = f"http://{remote_service_map[service]}/api/{version}/{service}/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=data, headers=headers) as response:
            if response.headers.get('Content-Type') == 'application/json':
                data = await response.json()
            else:
                data = await response.text()
            return response.status, data
