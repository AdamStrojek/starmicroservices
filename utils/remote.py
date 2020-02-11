import aiohttp


remote_service_map = {
    "auth": "auth:5040",
    'resource': 'resource:5050'
}


async def call_remote(service, endpoint, headers: dict, version='v1', **data):
    url = f"http://{remote_service_map[service]}/api/{version}/{service}/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=data) as response:
            data = await response.json()
            print(resp.status)
            print(data)
            return resp.status, data
