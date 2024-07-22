import requests
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import ClassVar, Dict

app = FastAPI(debug=True)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

class DiscordWebhook(BaseModel):
    webhookurl: str
    secretkey: str
    data: ClassVar[Dict[str, str]] = {
        "content": "data"
    }

ActiveKey = "SFGFvsdcvwer034e032044tsdfvrdg43t345rwef91209319832reiwe9fhvh43rt234523-r-sdfmnsefg3=eq3rwefdsfsedgerhgeryhg435234`123qwdasdasdwfawf3weq4213"

@app.post("/v1/d/")
async def webhookpost(item: DiscordWebhook):
    if item.secretkey == ActiveKey:
        if not item.webhookurl.startswith(("https://discord.com/api/", "http://discord.com/api/")):
            return {"Error": "409", "Info": "Invalid URL"}

        response = requests.post(item.webhookurl, json=item.data)

        return {"Status": response.status_code, "Data": response.content.decode()}
    else:
        return {"Status": 500, "Error": "Invalid Server Access Key"}
