#to import geonames into pandas, was erronoeois with normal read_csv but based on [this](https://github.com/scrapinghub/webstruct/blob/master/webstruct/gazetteers/geonames.py) solved 

db=pd.read_csv('IN.txt', delimiter="\t")
db=pd.read_csv('IN.txt', delimiter="\t", header=None, names=['countryCode','postalCode','placeName','adminName1','adminCode1','adminName2','adminCode2','adminName3','adminCode3','latitude','longitude','accuracy'])
db2=db[db['admin name2'].str.contains("Coimbatore")]




columns=['geonameid','name','asciiname','alternatenames','latitude','longitude','feature class','feature code','country code','cc2','admin1 code', 'admin2 code', 'admin3 code', 'admin4 code', 'population','elevation','dem', 'timezone','modification date']





names=['country code','postal code','place name','admin name1','admin code1','admin name2','admin code2','admin name3','admin code3','latitude','longitude','accuracy']         
