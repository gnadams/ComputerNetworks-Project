from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from datetime import datetime

from sqlalchemy.orm import Session
from Sql_app import models, schemas, crud
from Sql_app.database import SessionLocal, engine




models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

bandwidth = schemas.ItemBase
bandwidth.error = True
bandwidth.upload = 0
bandwidth.download = 0
bandwidth.time = ""


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def name(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "bandwidth": bandwidth})

@app.get("/bandwidth")
async def receive_bandwidth():
    if bandwidth.error != True:
        return {"upload": bandwidth.upload, "download": bandwidth.download, "ping":bandwidth.ping, "time":bandwidth.time}
    else:
        return {"Error": "Bandwidth has not been uploaded yet"}
    #speed = get_network_speed()
    #return speed
    #if speed["error"] == "False":
    #    return speed
    #else:
    #    return {"error": "True"}



@app.post("/upload") #, response_model=schemas.ItemBase
async def upload_bandwidth(item: schemas.ItemBase, db: Session = Depends(get_db)):
    item_dict = item.dict()
    bandwidth1 = schemas.ItemBase
    if item_dict["error"] != True:
        bandwidth1.error = False
        bandwidth1.upload = float(item_dict["upload"])
        bandwidth1.download = float(item_dict["download"])
        bandwidth1.upload = round(bandwidth1.upload, 1)
        bandwidth1.download = round(bandwidth1.download, 1)
        bandwidth1.time = item_dict["time"]
        return(crud.create_bw(db, bandwidth1))
    return item_dict

