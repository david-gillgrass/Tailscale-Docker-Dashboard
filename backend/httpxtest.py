import httpx
import asyncio
import json

async def ping():

    with open('user_services.JSON','r',encoding='UTF-8') as file:
        services  = json.load(file)

    async with httpx.AsyncClient() as client:

        for service in services:
            try:
                r = await client.get(service["LAN_URL"], timeout = 1.0000)
                print(f'Connection Successful to {service["Name"]} via {service["LAN_URL"]}', r.status_code)
            except httpx.ConnectTimeout as exc:
                    print(f'Error while connecting to {exc.request.url!r}, Trying Tailscale!')
                    try:
                        r = await client.get(service["Tailscale_URL"], timeout= 1.000)
                        print(f'Connection Successful to {service["Name"]} via {service["Tailscale_URL"]}')
                    except httpx.ConnectTimeout as exc:
                        print(f'Error while connecting to: {exc.request.url!r}')

    
asyncio.run(ping())