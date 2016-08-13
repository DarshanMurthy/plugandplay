import json, requests
import math
#import matplotlib.pyplot as plt
import numpy as np

def calculateDistance(x1,y1,x2,y2):
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
     return dist

url = 'https://sensor-api.thinnect.net/api/v0/devices/'
# url = 'https://sensor-api.thinnect.net/api/v0/data/'

params = dict(
    limit=1000,
    offset=0
)


resp = requests.get(url=url, params=params)
data = json.loads(resp.text)['devices']
lat=[]
lon=[]
r_lat=[]
r_lon=[]
for d in data:
	if d['latitude'] != 0.0:
		# if d['name'] not in ['150', '99', '98']:

		lat.append(d['latitude'])
		lon.append(d['longitude'])

		dist =calculateDistance(d['latitude'],d['longitude'],d['latitude'],d['longitude'])
		#print(dist)


		# else:
		# 	r_lat.append(d['latitude'])
		# 	r_lon.append(d['longitude'])

#fig = plt.figure()
#ax = fig.add_subplot(111)


# offset=min(min(lat), min(lon))
# offset = 1500
# scale = 500
# lat=map(lambda x: x*scale+offset, lat)
# lon=map(lambda x: x*scale, lon)

# im = plt.imread('floor.png')
# implot = ax.imshow(im)

#ax.scatter(lon, lat, c='black')





dist = lambda p1, p2: math.sqrt((p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
thresh=0.35
points=[(int(d['name']), d['latitude'], d['longitude']) for d in data if d['name'] != None and d['name'] not in ['0', '150', '129', '127', '128', '130'] and d['latitude'] != 0.0 ]
neighbors={}
for i in range(1, 126):
	neighbors[i] = []

for p1 in points:
	for p2 in points:
		if (p1 != p2) and (dist(p1, p2) < thresh):
			neighbors[p1[0]].append(p2[0])
			neighbors[p1[0]]=sorted(neighbors[p1[0]])

[neighbors.pop(key) for key, value in zip(neighbors.keys(), neighbors.values()) if len(value) == 0]
s='{\n'
for key, value in neighbors.iteritems():
	s += '\t' + str(key) + ' : ' + str(value) + '\n'
s += '}'
print s

#print json.dumps(neighbors, indent=2)
# for n in neighbors.keys():
# 	print n, neighbors[n]

# i=0


# list1=[]
# list2=[]
# temp=(0,0)
# for d in data:
# 	list1.append(d['latitude'])
# 	list2.append(d['longitude'])
# for i in range(127):
# 	for j in range(127):
# 		dist=calculateDistance(list1[i],list2[i],list1[j],list2[j])
# 		print(dist)





	#ax.annotate(data[i]['name'], xy=xy, textcoords='data')
	#i += 1
# plt.scatter(r_lon, r_lat, c='red', s=50)
#plt.show()