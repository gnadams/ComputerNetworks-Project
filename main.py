from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

class Item(BaseModel): # class for storing bandwidth
    error: bool
    upload: float
    download: float
    ping: float
    time: str


app = FastAPI()

bandwidth = Item
bandwidth.error = True
bandwidth.upload = 0
bandwidth.download = 0
bandwidth.ping = 0


@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/bandwidth")
async def receive_bandwidth():
    if bandwidth.error != True:
        return {"upload": bandwidth.upload, "download": bandwidth.download, "ping":bandwidth.ping}
    else:
        return {"Error": "Bandwidth has not been uploaded yet"}
    #speed = get_network_speed()
    #return speed
    #if speed["error"] == "False":
    #    return speed
    #else:
    #    return {"error": "True"}



@app.post("/upload")
async def upload_bandwidth(item: Item):
    item_dict = item.dict()
    if item_dict["error"] != True:
        bandwidth.error = False
        bandwidth.upload = item_dict["upload"]
        bandwidth.download = item_dict["download"]
        bandwidth.ping = item_dict["ping"]
        bandwidth.time = item_dict["time"]
    return item_dict