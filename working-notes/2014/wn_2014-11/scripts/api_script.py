import json
import urllib2

url = "https://maps.googleapis.com/maps/api/geocode/json?address=SRIRAMAKRISHNAENGINEERINGCOLLEGE+Vattamalaipalayam+NGGOColonyPost+Coimbatore+641022&key=APIkey"

import pandas as pd
db=pd.read_csv('Coimbatore_postal.csv')

#names=db['placeName_1'].tolist()
#empty sapce in names gives url error
#db["placeName_1"] = df["placeName"].map(str.strip)
#to overcome above error used 
db['placeName_1'] = db['placeName'].str.replace(' ', '+')
db['placeName_2'] = db['placeName_1'].str.replace('.', '+')
names=db['placeName_2'].tolist()
data = json.load(urllib2.urlopen(url))
a=[]
for name in names:
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+name+"&key=APIkey"
	data = json.load(urllib2.urlopen(url))
	a.append(data)
	




ouputfilename='loc_latA1.json'
with open(outputfilename, 'wb') as outfile:
     json.dump(a, outfile)


print data
