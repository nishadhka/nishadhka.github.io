import shapefile as shp
import pandas as pd
import csv
import os
import sys


db0=pd.read_csv('IN.txt', delimiter="\t", header=None, names=['countryCode','postalCode','placeName','adminName1','adminCode1','adminName2','adminCode2','adminName3','adminCode3','latitude','longitude','accuracy'])
db1=db0[db0['adminName2'].str.contains("Coimbatore")]
db2=db.drop_duplicates(cols='postalCode', take_last=True)

db2.to_csv('Coimbatore_postal2.csv')

db=pd.read_csv('Coimbatore_postal2.csv')
#read data from csv file and store in lists
#with open(fileToOpen, 'r') as csvfile:
#    r = csv.reader(csvfile, delimiter=";")
#    for i,row in enumerate(r):
#        print row
#        if i > 0: #skip header
#            fid_nr.append(row[2])
#            x.append(float(row[0]))           
#            y.append(float(row[1]))         
#            angle.append(int(row[3]))         

#Set up shapefile writer and create empty fields
w = shp.Writer(shp.POINT)
w.autoBalance = 1 #ensures gemoetry and attributes match
w.field("postalCode","N",10)
w.field("longitude","F",10,8)
w.field("latitude","F",10,8)
w.field("placeName","C",30)
w.field("adminName1","C",30)
w.field("adminName2","C",30)
w.field("adminName3","C",30)
w.field("accuracy","C",5)




#loop through the data and write the shapefile
for j,k in enumerate(db.longitude):
    w.point(k,db.latitude[j]) #write the geometry
    w.record(db.postalCode[j],db.longitude[j],db.latitude[j],db.placeName[j],db.placeName[j],db.adminName1[j],db.adminName2[j],db.adminName3[j],db.accuracy[j])
#this gives error of unidentifuiable like this ```File "hashtable.pyx", line 388, in pandas.hashtable.Int64HashTable.get_item (pandas/hashtable.c:6517)
#KeyError: 0
```
#this was reproducecd in 
#for j,k in enumerate(db2.longitude):
#     a=db2.latitude[j]
#     print k,a
#The baove problem was solved IF I am getting the dataframe from a csv file, a problem related with pandas dataframe


    
#Save shapefile
out_file='Coimbatore_postalcode1.shp'
w.save(out_file)
print "Done!"
