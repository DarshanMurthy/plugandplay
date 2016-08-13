import requests
import  json

param = dict(limit=10002, offset=0)
data = requests.get('https://sensor-api.thinnect.net/api/v0/data/',param)
print(data.text)

for keys in json.loads(data.text):
    print(keys)


#{u'source': u'70B3D5E390000112', u'type': u'dt_movement_count',
# u'end': u'2016-07-24T23:54:02', u'value': 2917.0, u'start': u'2016-07-24T23:54:02'}

#print(data.json()['data'][0]['type'])

# We are getting the details in every second
count =0
while count<1000:
    if data.json()['data'][count]['type'] == 'dt_movement_count' and data.json()['data'][count]['source']=='70B3D5E390000153':
        print(data.json()['data'][count]['source'],data.json()['data'][count]['value'])
        #print(data.json()['data'][count]['start'], data.json()['data'][count]['end'])
        #print(data.json()['data'][count]['start'],data.json()['data'][count]['end'])

        #print(data.json()['data'][count]['source'],data.json()['data'][count]['type'],data.json()['data'][count]['value'])
    count = count + 1

