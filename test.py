import requests
import json
from datetime import *
from pytz import timezone

GLOBAL_URL = "https://computernetworks-project.onrender.com/"
LOCAL_URL = "http://127.0.0.1:8000/" 

tz = timezone('EST')
time_now = datetime.now(tz)#.strftime("%m/%d/%Y, %H:%M:%S")
time_now = str(time_now)
body = {
  "error": False,
  "upload": 400.512341234,
  "download": 400.4512341243,
  "date": time_now,
  "ping" : 0,
  "id": 0,
}
json_data = json.dumps(body)


r = requests.post(LOCAL_URL+"upload", data=json_data)
