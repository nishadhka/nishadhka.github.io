import json

data = []
with open('loc_latA2.json') as f:
    for line in f:
        data.append(json.loads(line))


loc_latA2.json


db=pd.read_json('loc_latA2.json')
data=db['results'].tolist()


x = json.loads('loc_latA2.json')


import json
import csv

with open("loc_latA2.json") as file:
    data = json.load(file)

with open("loc_latA2.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item[0]['results'][0]['formatted_address']])


f = open('loc_latA2.json')
data = json.load(f)
f.close()

f=csv.writer(open('test.csv','wb+'))

for item in data:
	f.writerow([item['results']['geometry']['location'], item['results']['formatted_address']])


pd.Panel("loc_latA2.json")

from pandas.io.json import json_normalize
path = mf.getPath('loc_latA2.json')
f = open('loc_latA2.json')
data = json.load(f)
testTrials = json_normalize(data[0]['results'])
#result in error of list indices must be intger not string

for i in range(len(data)):
	testTrials = json_normalize(data[i]['results'])


jsonResponse=json.load(f)
a=[]
for i in range(610):
	est = json.dumps([s['geometry']['location'] for s in jsonResponse[i]['results']], indent=3)
	a.append(est)


b=[]
for i in range(610):
	est = json.dumps([s['address_components']['formatted_address'] for s in jsonResponse[i]['results']], indent=3)
	b.append(est)

b=[]
for i in range(610):
	est = json.dumps([s['address_components']['long_name'] for s in jsonResponse[i]['results']], indent=3)
	b.append(est)

#to query list of dictonaries
data[0]['results'][0]['formatted_address']
u'Pappampatti, Tamil Nadu 641016, India'
data[0]['results'][0]['geometry']['location']

a=[]
for i in range(4)):
	a=data[i]['results'][0]['formatted_address']
	b=data[i]['results'][0]['geometry']['location']
	c=a+b
	a.append(c)



db=pd.read_json('loc_latA2.json')
data=db['results'].tolist()
keys = ['formatted_address']
f = open('people.csv', 'wb')
dict_writer = csv.DictWriter(f, keys)
dict_writer.writer.writerow(keys)
dict_writer.writerows(data)



def flatten(l):
'''
flattens a list, dict or tuple
'''
    ret = []
    for i in l:
        if isinstance(i, list) or isinstance(i, tuple):
            ret.extend(flatten(i))
        elif isinstance(i, dict):
            ret.extend(flatten(i.items()))
        else:
            ret.append(i)
    return ret


test_file = ()
length = len(data)
with open('test1.csv', 'wb') as test_file:
     csv_writer = csv.writer(test_file, delimiter=',')
     for y in range(length):
         line = flatten(data[y])
         csv_writer.writerow([x for x in line])


data=pd.read_json('loc_latA2.json')
data['wer'] = db['results'].str.replace('[', '')
x = pd.read_json(data)['results'].iloc[0]

db=pd.read_json('loc_latA2.json')
data=db['results'].tolist()
pdf = db.pivot("results")
d = {k: v.tolist() for k,v in pdf.iterrows()}	

for key, val in dd.items():
     w.writerow([key, val])


#to query list of dictonaries, but having problem in nill values
f = open('loc_latA2.json')
data = json.load(f)
f.close()
a=data[0]['results'][0]['formatted_address']
b=data[0]['results'][0]['geometry']['location']['lat']
b2=data[0]['results'][0]['geometry']['location']['lng']
c4=aa+str(b)+str(b2)
da=str(aa)+'//'+str(b)+','+str(b2)



#working function to avoid nill valiue problem
jsonData = """{"from": {"id": "8", "name": "Mary Pinter"}, "message": "How ARE you?", "comments": {"count": 0}, "updated_time": "2012-05-01", "created_time": "2012-05-01", "to": {"data": [{"id": "1543", "name": "Honey Pinter"}, {"name": "Joe Schmoe"}]}, "type": "status", "id": "id_7"}"""

def getTargetIds(jsonData):
    data = json.loads(jsonData)
    for dest in data['to']['data']:
        print("to_id:", dest.get('id', 'null'))

#testing for for loop both index and element in a list for above requierment of for loop json with index and element
data2=data[:8]
for index, elem in enumerate(data2):
        print(index, elem)

for i, elem in enumerate(data2):
	a=data2[i]['results'][0]['formatted_address']
	b=data2[i]['results'][0]['geometry']['location']['lat']
	b2=data2[i]['results'][0]['geometry']['location']['lng']
	c4=a+'//'+str(b)+','+str(b2)
  	print i
	print c4

#implementing taking caare of null json elements
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		for elem in data2[i]['results'][0]:
			print("to_id:", elem.get('formatted_address', 'null'))
#above ends in error saying that ```AttributeError: 'unicode' object has no attribute 'get'```
#Another try A1
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get("results", "null"))
getTargetIds(data2)
#But above is working, thoughing results
#Another imporvment A2
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get("'results','formatted_address'", "null"))
getTargetIds(data2)
#thoruhgin null value for all
#Another imporvment A3
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get(elem[i]['results'][0]['formatted_address'], "null"))
getTargetIds(data2)
#thoruhgin key error
#Another imporvment A4
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get("results[0]formatted_address", "null"))
getTargetIds(data2)
#thoruhgin all null value
#Another imporvment A5
def getTargetIds(data2):
	for i, elem in enumerate(data2['results']):
		print("to_id:", elem.get("formatted_address", "null"))
getTargetIds(data2)
#thoruhgin TypeError: list indices must be integers, not str
#Another imporvment A6
def getTargetIds(data2):
	for i, elem in enumerate(data2['results'][0]):
		print("to_id:", elem.get("formatted_address", "null"))
getTargetIds(data2)
#thoruhgin TypeError: list indices must be integers, not str
#Another imporvment A7
def getTargetIds(data2):
	for i, elem in enumerate(data2['results']):
		print("to_id:", elem.get("[0]", "null"))
getTargetIds(data2)
#thoruhgin TypeError: list indices must be integers, not str
#Another imporvment A8
def getTargetIds(data2):
	for i, elem in enumerate(data2[i]['results']):
		print("to_id:", elem.get([0], "null"))
getTargetIds(data2)
#thoruhgin UnboundLocalError: local variable 'i' referenced before assignment
#Another imporvment A9
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get("results[0]formatted_address", "null"))
getTargetIds(data2)
#thoruhgin all null value
#Another imporvment A10
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		print("to_id:", elem.get("['results'][0]['geometry']['location']['lat']", "null"))
getTargetIds(data2)
#thoruhgin all null value
#it seems only way is to get the null return value list and work on that
#Another imporvment A11
b=[]
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		b.append("to_id:", elem.get("results", "null"))
getTargetIds(data2)
# though TypeError: append() takes exactly one argument (2 given)
#Another imporvment A12
b=[]
def getTargetIds(data2):
	for i, elem in enumerate(data2):
		a=("to_id:", elem.get("results", "null"))
                b.append(a)
getTargetIds(data2) 
# this is cylcing, now comes to first problem of start
# so trying with pandas to remove the null values and then for loop on it
#Another imporvment A13
db=pd.read_json('loc_latA2.json')
df = db[db.status != 'ZERO_RESULTS']
data=df['results'].tolist()
data2=data[:8]
for i, elem in enumerate(data2):
	a=data2[i]['results'][0]['formatted_address']
	b=data2[i]['results'][0]['geometry']['location']['lat']
	b2=data2[i]['results'][0]['geometry']['location']['lng']
	c4=a+'//'+str(b)+','+str(b2)
  	print i
	print c4
#returns error of TypeError: list indices must be integers, not str, this for all other try similart o this type querry
#but this giving more hope
#Another imporvment A14
b=data2[0]
c=b[0]
b=c['geometry']['location']['lat']
ds=[]
for i, elem in enumerate(data2):
	b=data2[i]
	c=b[0]
	add=c['formatted_address']
	lat=c['geometry']['location']['lat']
	lng=c['geometry']['location']['lng']
	c4=add+'//'+str(lat)+','+str(lng)
	ds.append(c4)

#gives correct result, so looping with above conditions may turn good, YES!!! it returns correct let me go with full json
#another imporvment A15 
dp=[]
for i, elem in enumerate(data):
	b=data[i]
	c=b[0]
	add=c['formatted_address']
	lat=c['geometry']['location']['lat']
	lng=c['geometry']['location']['lng']
	c4=add+'//'+str(lat)+','+str(lng)
	dp.append(c4)

#another imporvment A16
db=pd.read_json('loc_latA2.json')
df = db[db.status != 'ZERO_RESULTS']
data=df['results'].tolist()
dp=[]
for i, elem in enumerate(data):
     b=data[i]
     c=b[0]
     add=c['formatted_address']
     lat=c['geometry']['location']['lat']
     lng=c['geometry']['location']['lng']
     c4=add+'//'+str(lat)+','+str(lng)
     dp.append(c4)
#the above step of 'c=b[0]' is cruicial othetr wise the list based dictonary won't be queried or pandas dictonary column can't be quieried
latlon = pd.DataFrame(dp)
dpsp=[]
for i in dp:
     sp=re.split('//',i)
     dpsp.append(sp)
latlon = pd.DataFrame(dpsp)
latlon.columns=['address','lonlat']
sd=latlon['address'].tolist()
sdp=[]
for i in sd:
     p=re.findall(r'\b\d+\b',i)
     sdp.append(p)
#sdp1=[item for sdp in l for item in sdp]
#the above didn't worked to flatten the list other wise pandas create two columns
sdp1=list(itertools.chain(*sdp))
#lat=zip(dpsp, sdp)
latlon['pincode']= pd.DataFrame(sdp1)
latlon['placeName_3'] = latlon['address'].str.replace(',', ' ')
latlon['placeName_3'] = latlon['placeName_3'].str.replace(' ', '+')


db=pd.read_csv('Coimbatore_postal.csv')
db['placeName_1'] = db['placeName'].str.replace(' ', '+')
db['placeName_2'] = db['placeName_1'].str.replace('.', '+')
db['adminName1_1']= db['adminName1'].str.replace(' ', '+')
db['pc']=db['postalCode'].apply(str)
db['placeName_3'] = db['placeName_1']+'+'+db['adminName2']+'+'+db['pc']+'+'+db['adminName1_1']


points=latlon.merge(db, on="placeName_3")
#fail return 0 row dataframe
latlon.columns=['address','lonlat','postalCode','placeName_3']

points=latlon.merge(db, on="postalCode")
#this also error, no row written
pt=pd.merge(db, latlon, how='left', left_on='postalCode', suffixes=('', '.1'))
#this return in error of no len
mdf = pd.merge(db,latlon,on='postalCode')
mdf = pd.merge(db,latlon,on='placeName_3')

mdf1=pd.merge(latlon, db, left_on='postalCode', right_on='pc', how='inner')
latlon1=latlon[:5]
db1=db[:5]
mdf1=pd.merge(latlon1, db1, left_on='postalCode', right_on='pc', how='inner')

#so alternatoiive is to find the empty emelent in the list, its index, remove those elements and re run the for loop

