import requests
import json
url="https://sensor-api.thinnect.net/api/v0/data/?limit=1000"
def fun():
    param = dict(limit=1000, offset=0)
    request =requests.get(url,params=param)
    length =len(json.loads(request.text)['data'])
    value = json.loads(request.text)
    for key in value:
        print(key)

fun()