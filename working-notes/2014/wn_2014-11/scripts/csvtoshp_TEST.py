import shapefile as shp
import csv
import os
import sys


db=pd.read_csv('test.csv', delimiter=";")

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
w.field("fid_nr","N")
w.field("x","F",10,8)
w.field("y","F",10,8)
w.field("angle","N",4)    

#loop through the data and write the shapefile
for j,k in enumerate(db.x):
    w.point(k,db.y[j]) #write the geometry
    w.record(db.fid_nr[j],db.x[j],db.y[j],db.angle[j])
#Save shapefile
out_file = 'GPS_Pts.shp'
w.save(out_file)

