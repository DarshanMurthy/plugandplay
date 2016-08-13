import json, requests
import matplotlib.pyplot as plt
import numpy as np

loc_url='http://connected-lighting.net/data/devices'
resp = requests.get(url=loc_url)
data = json.loads(resp.text)
print [d['sensorId'] for d in data]
lat=[]
lon=[]
r_lat=[]
r_lon=[]
office=0
startup=0
office_temp=0
startup_temp=0
temp=[]
# locations=set()
all_locs=[]
for d in data:
	loc=[np.float(x) for x in d['location'].split(',')]

	# locations.add(tuple(loc))
	# all_locs.append(tuple(loc))
	# print loc
	if d['type'] == 'Motion':
		if d['sensorId'] not in ['16', '91', '126']:
			lat.append(loc[0])
			lon.append(loc[1])
		else:
			r_lat.append(loc[0])
			r_lon.append(loc[1])
		if d['area'] == 'office':
			office+=1
		elif d['area'] == 'startup':
			startup+=1
	else:
		temp.append(loc)
		if d['area'] == 'office':
			office_temp+=1
		elif d['area'] == 'startup':
			startup_temp+=1


print len(lat), len(temp)
# print len(locations)
print office, startup, office_temp, startup_temp
offset=min(min(lat), min(lon))-150
scale=1
lat=map(lambda x: (x-offset)*scale, lat)
lon=map(lambda x: (x-offset)*scale, lon)

im = plt.imread('floor.png')
implot = plt.imshow(im)

# plt.scatter(lat[5], lon[5], c='green', alpha=0.3, s=200)
# for n in locations:
# 	lat1 = n
# 	plt.scatter(lat1[0], lat[1], c='red', alpha=0.3, s=200)
# duplicates=[]
# for x in locations:
# 	if list(all_locs).count(x) > 1:
# 		duplicates.append(x)
# duplicates=[x if (list(locations).count(x) > 1) for x in all_locs]
# print duplicates
# for l in duplicates:
# 	plt.scatter(l[0], l[1], c='red', alpha=0.3, s=200)
for l in temp:
	plt.scatter(l[0], l[1], c='red', alpha=0.3, s=200)
plt.scatter(lat, lon, c='black')
plt.scatter(r_lat, r_lon, c='red', s=50)

plt.axis('off')
plt.show()