from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

origins=[
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return{"Message":"Hello World"}

@app.get("/Services")
def read_services():
    with open('user_services.JSON','r', encoding='UTF-8') as file:
        services = json.load(file)
        return{"Services": services}

@app.get("/servicestest")

async def ping():

    services_tested = []

    with open('user_services.JSON','r',encoding='UTF-8') as file:
        services  = json.load(file)

    async with httpx.AsyncClient() as client:

        for service in services:
            try:
                r = await client.get(service["LAN_URL"], timeout = 1.0000)
                # print(f'Connection Successful to {service["Name"]} via {service["LAN_URL"]}', r.status_code)
                services_tested.append({"Name":service["Name"],"Address":service["LAN_URL"],"Connection Type":"HTTP", "Status":"UP"})
            except httpx.ConnectTimeout:
                    try:
                        r = await client.get(service["Tailscale_URL"], timeout= 1.000)
                       # print(f'Connection Successful to {service["Name"]} via {service["Tailscale_URL"]}')
                        services_tested.append({"Name":service["Name"],"Address":service["Tailscale_URL"],"Connection Type":"Tailscale", "Status":"UP"})
                    except httpx.ConnectTimeout:
                        services_tested.append({"Name":service["Name"],"Address":"Null","Connection Type":"Both", "Status":"DOWN"})

    return{"ServicesTested": services_tested}

