import requests
import  json
sensors = requests.get('https://sensor-api.thinnect.net/api/v0/devices/')
# Source Details
source=0
while source<127:
    source = source + 1
    #print(sensors.json()['devices'][source]['source'])

# Location where sensors are stored
latitude=0
logitude=0
while latitude<127:
    latitude = latitude + 1
    print(sensors.json()['devices'][latitude]['latitude'],sensors.json()['devices'][latitude]['longitude'])

name=0
while name<127:
    name = name + 1
    #print(sensors.json()['devices'][name]['name'])

data = requests.get('https://sensor-api.thinnect.net/api/v0/data/')

for keys in data.json():
    print (keys)


print(data.json()['data'])





