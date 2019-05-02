import pandas
import pandas as pd
d=pd.read_csv('/home/swl-sacon-dst/Documents/GISE_2013/LAB/Aerocet_DATA/Oct_sample/json/A08102014M.csv')
db=d[['Time','long','lat','PM1(ug/m3)','PM2.5(ug/m3)','PM4(ug/m3)','PM7(ug/m3)','PM10(ug/m3)','TSP(ug/m3)']]
db['geojson']='{\\"type\\":\\"Point\\",\\"coordinates\\":['+db['long'].astype(str)+','+db['lat'].astype(str)+']}'
db2=db[['Time','PM2.5(ug/m3)','PM10(ug/m3)','TSP(ug/m3)','geojson']]

df.apply(lambda x:'%s is %s' % (x['bar'],x['foo']),axis=1)




import csv
import sys
import json
f=open('A08102014M.csv', 'r')



db2.to_json('testJS3.json')
db2.reset_index().to_json('testJS4.json',orient='index')
>>> db2.to_json('testJS4.json',orient='index')
>>> db2.to_json('testJS5.json',orient='index')
>>> import csv
>>> import sys
>>> import json
>>> f=open('A08102014M.csv', 'r')
>>> fieldnames=['Time','PM2.5(ug/m3)','PM10(ug/m3)','TSP(ug/m3)','geojson']
>>> csv_reader = csv.DictReader(f,fieldnames)
>>> csv_reader
<csv.DictReader instance at 0x29497a0>
>>> data = json.dumps([r for r in csv_reader])
>>> data



print json.dumps(db2.as_matrix().tolist(),indent=4)


import pandas
import json
import pandas as pd
data=pd.read_csv('/home/swl-sacon-dst/Documents/GISE_2013/LAB/Aerocet_DATA/Oct_sample/json/A08102014M.csv')
db=data[['Time','long','lat','PM2.5(ug/m3)','PM10(ug/m3)','TSP(ug/m3)']]
db['geojson']='{\"type\":\"Point\",\"coordinates\":['+db['long'].astype(str)+','+db['lat'].astype(str)+']}'
d = [
	dict([
		(colname, row[i])
		for i,colname in enumerate(db.columns)
	])
	for row in df.values
]

#alternative to above which gives error of IndexError: index out of bounds
d = [{colname : row[i] for i, colname in enumerate(db.columns)} for row in db.iterrows()]
#alternative to above with error of IndexError: tuple index out of range
d=[{k:db.values[i][v] for v,k in enumerate(db.columns)} for i in range(len(db)) ]
#the above only is working and genrated the json as of the meteros example, based on [this](https://gist.github.com/mikedewar/1486027)
jsonf = open('testJS7.json','w')
dd=json.dumps(d)
jsonf.write(dd)
jsonf.close()

