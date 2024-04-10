import requests
import json

STATIC_URL = "https://computernetworks-project.onrender.com/"
body = {
  "error": False,
  "upload": 400,
  "download": 400,
  "ping": 50
}
json_data = json.dumps(body)



r = requests.post(STATIC_URL+"upload", data=json_data)