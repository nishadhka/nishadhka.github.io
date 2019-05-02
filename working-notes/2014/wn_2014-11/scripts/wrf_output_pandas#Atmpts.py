from netCDF4 import Dataset
import numpy as np
import os
#here importing wrf output file into python
wrfoutput = 'wrfout_d01_2014-06-05_05:00:00_D03'

#converting lat long value into 1D numpy array
fh = Dataset(wrfoutput, mode='r')
lons = fh.variables['XLONG'][:]
lats = fh.variables['XLAT'][:]
lons.shape
lonsX0=lons.reshape((105,96))
lonsX=lonsX0.reshape((10080))
latsX0=lats.reshape((105,96))
latsX=latsX0.reshape((10080))
#here cliping array into Coimbatore region of (76.16,10.86) and (76.79, 11.23), index value (333:1666) was known from 
#the index value of lat by doing, y=np.where(latsX==10.86), y=np.where(latsX==11.23)
cbeX=lonsX[333:1666]
cbeY=latsX[333:1666]

os.popen(ncl 'file_in="+i+"' 'file_out="'''+i+''''WRFPOST''''+'''"' wrfout_to_cf.ncl''')

a="ncl 'file_in="+i+"' 'file_out="+i+WRFPOST'


a='''ncl 'file_in="'''+i+'''"' 'file_out="'''+i+'''wrfpost.nc"' wrfout_to_cf.ncl'''
os.popen(a)



a='''ncl 'file_in="wrfout_d01_2014-06-05_00:00:00_D03"' 'file_out="wrfpost.nc"' wrfout_to_cf.ncl'''
os.popen(a)

#to make into module program
#the program does is read file name in the folder, convert wrfoutput nc into wrfpost, query wrf ouputnc and post nc





def conpost():
	wrfout=folred()
	for i in wrfout:
		a='''ncl 'file_in="'''+i+'''"' 'file_out="'''+i+'''wrfpost.nc"' wrfout_to_cf.ncl'''
		os.popen(a)

def folreadwrfout():
        path = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/wrf_output_python/'
        wrfout = [f for f in os.listdir(path) if f.endswith('D03')]
	return wrfout

def folreadwrfpost():
        path = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/wrf_output_python/'
        wrfpost = [f for f in os.listdir(path) if f.endswith('.nc')]
	return wrfpost

data = pd.DataFrame()
def ncwopandas():
	wo=folreadwrfout()
	time,lat,lon=[],[],[]
	for i in wo:
		fh = Dataset(i, mode='r')
		lons = fh.variables['XLONG'][:]
		lats = fh.variables['XLAT'][:]
		lonsX0=lons.reshape((105,96))
		lonsX=lonsX0.reshape((10080))
		latsX0=lats.reshape((105,96))
		latsX=latsX0.reshape((10080))
		cbeX=lonsX[333:1666]
		cbeY=latsX[333:1666]
		tm=fh.variables['Times'][:]
		tm0=tm.reshape((19))
		tm1 = "".join(tm0)
		time.append(tm1)
		lon.append(cbeX)
		lat.append(cbeY)
	return time, lat, lon



a=fh.variables['Times'][:]



import itertools
li2 = list(itertools.chain(*a))

tm=fh.variables['Times'][:]
tm0=tm.reshape((19))
time = "".join(lonsX0)



wo=folreadwrfout()
lat,lon=[],[]
for i in wo:
	fh = Dataset(i, mode='r')
	lons = fh.variables['XLONG'][:]
	lats = fh.variables['XLAT'][:]
	lonsX0=lons.reshape((105,96))
	lonsX=lonsX0.reshape((10080))
	latsX0=lats.reshape((105,96))
	latsX=latsX0.reshape((10080))
	cbeX=lonsX[333:1666]
	cbeY=latsX[333:1666]
	lon.append(cbeX)
	lat.append(cbeY)


#creating numpy array with fromiter

def ncwopandas():
	wo=folreadwrfout()
	for i in wo:
		fh = Dataset(i, mode='r')
		lons = fh.variables['XLONG'][:]
		lats = fh.variables['XLAT'][:]
		lonsX0=lons.reshape((105,96))
		lonsX=lonsX0.reshape((10080))
		latsX0=lats.reshape((105,96))
		latsX=latsX0.reshape((10080))
		return cbeX=lonsX[333:1666]
		return cbeY=latsX[333:1666]

a=np.fromiter(ncwopandas(), dtype=int)	


#Atempt 2, to get the array from wrf output, it is working

def ncwopandas():
     wo=folreadwrfout()
     time,lat,lon=[],[],[]
     for i in wo:
             fh = Dataset(i, mode='r')
             lons = fh.variables['XLONG'][:]
             lats = fh.variables['XLAT'][:]
             lonsX0=lons.reshape((105,96))
             lonsX=lonsX0.reshape((10080))
             latsX0=lats.reshape((105,96))
             latsX=latsX0.reshape((10080))
             cbeX=lonsX[333:1666]
             cbeY=latsX[333:1666]
             tm=fh.variables['Times'][:]
             tm0=tm.reshape((19))
             tm1 = "".join(tm0)
             time.append(tm1)
             lon.append(cbeX)
             lat.append(cbeY)
      return time, lat, lon
 
time1,lat1,lon1=ncwopandas()
time2=np.array(time1)
lat2=np.array(lat1)
lon2=np.array(lon1)

#attempt 3, for adding the PM25 and PM10 variables
def ncwopandas():
     wo=folreadwrfout()
     time,lat,lon,pm25,pm10=[],[],[],[],[]
     for i in wo:
             fh = Dataset(i, mode='r')
             lons = fh.variables['XLONG'][:]
             lats = fh.variables['XLAT'][:]
             lonsX0=lons.reshape((105,96))
             lonsX=lonsX0.reshape((10080))
             latsX0=lats.reshape((105,96))
             latsX=latsX0.reshape((10080))
             cbeX=lonsX[333:1666]
             cbeY=latsX[333:1666]
             tm=fh.variables['Times'][:]
             tm0=tm.reshape((19))
             tm1 = "".join(tm0)
	     tm2=np.repeat(tm1, 1333)
	     BC1 =  fh.variables['BC1'][:]
	     BC1=BC1[:,0]
             BC1r=BC1.reshape((105,96))
             BC1d=BC1r.reshape((10080))
             cbeBC1 = BC1d[333:1666]
             BC2 =  fh.variables['BC2'][:]
             BC2=BC2[:,0]
             BC2r=BC2.reshape((105,96))
             BC2d=BC2r.reshape((10080))
             cbeBC2 = BC2d[333:1666]
             OC1 =  fh.variables['OC1'][:]
             OC1=OC1[:,0]
             OC1r=OC1.reshape((105,96))
             OC1d=OC1r.reshape((10080))
             cbeOC1 = OC1d[333:1666]
             OC2 =  fh.variables['OC2'][:]
             OC2=OC2[:,0]
             OC2r=OC2.reshape((105,96))
             OC2d=OC2r.reshape((10080))
             cbeOC2 = OC2d[333:1666]
             DUST_1 =  fh.variables['DUST_1'][:]
             DUST_1=DUST_1[:,0]
             DUST_1r=DUST_1.reshape((105,96))
             DUST_1d=DUST_1r.reshape((10080))
             cbeD1 = DUST_1d[333:1666]       
             DUST_2 =  fh.variables['DUST_2'][:]
             DUST_2=DUST_2[:,0]
             DUST_2r=DUST_2.reshape((105,96))
             DUST_2d=DUST_2r.reshape((10080))
             cbeD2 = DUST_2d[333:1666] 
             DUST_3 =  fh.variables['DUST_3'][:]
             DUST_3=DUST_3[:,0]
             DUST_3r=DUST_3.reshape((105,96))
             DUST_3d=DUST_3r.reshape((10080))
             cbeD3 = DUST_3d[333:1666]
             DUST_4 =  fh.variables['DUST_4'][:]
             DUST_4=DUST_4[:,0]
             DUST_4r=DUST_4.reshape((105,96))
             DUST_4d=DUST_4r.reshape((10080))
             cbeD4 = DUST_4d[333:1666]
             SEAS_1 =  fh.variables['SEAS_1'][:]
             SEAS_1=SEAS_1[:,0]
             SEAS_1r=SEAS_1.reshape((105,96))
             SEAS_1d=SEAS_1r.reshape((10080))
             cbeSS1 = SEAS_1d[333:1666]
             SEAS_2 =  fh.variables['SEAS_2'][:]
             SEAS_2=SEAS_2[:,0]
             SEAS_2r=SEAS_2.reshape((105,96))
             SEAS_2d=SEAS_2r.reshape((10080))
             cbeSS2 = SEAS_2d[333:1666]
             SEAS_3 =  fh.variables['SEAS_3'][:]
             SEAS_3=SEAS_3[:,0]
             SEAS_3r=SEAS_3.reshape((105,96))
             SEAS_3d=SEAS_3r.reshape((10080))
             cbeSS3 = SEAS_3d[333:1666]
             Temp =  fh.variables['T2'][:]
             Temp0=Temp.reshape((105,96))
             Temp1=Temp0.reshape((10080))
             cbeT = Temp1[333:1666]
             PSFC =  fh.variables['PSFC'][:]
             PSFC=PSFC.reshape((105,96))
             PSFC=PSFC.reshape((10080))
             cbePSFC = PSFC[333:1666]
             a=287.05*cbeT
             pd= cbePSFC/a
             P25 =  fh.variables['P25'][:]
             P25=P25[:,0]
             P25=P25.reshape((105,96))
             P25=P25.reshape((10080))
             cbeP25 = P25[333:1666]
             sulf =  fh.variables['sulf'][:]
             sulf=sulf[:,0]
             sulf=sulf.reshape((105,96))
             sulf=sulf.reshape((10080))
             cbeS = sulf[333:1666]
             PM25= pd*(cbeP25+1.375*cbeS+cbeBC1+cbeBC2+1.8*(cbeOC1+cbeOC2)+cbeD1+0.286*cbeD2+cbeSS1+0.0942*cbeSS2)
             PM10= pd*(cbeP25+(1.375*cbeS)+cbeBC1+cbeBC2+(1.8*(cbeOC1+cbeOC2))+cbeD1+cbeD2+cbeD3+(0.87*cbeD4)+cbeSS1+cbeSS2+cbeSS3)
             time.append(tm2)
             lon.append(cbeX)
             lat.append(cbeY)
	     pm25.append(PM25)
	     pm10.append(PM10)
     return time, lat, lon, pm25, pm10

time1,lat1,lon1,pm251,pm101=ncwopandas()
#ends with error of ValueError: need more than 3 values to unpack



#attempt 4 for adding pm25 and pm10
def ncwppandas():
     wo=folreadwrfout()
     for i in wo:
             fh = Dataset(i, mode='r')
	     BC1 =  fh.variables['BC1'][:]
	     BC1=BC1[:,0]
             BC1r=BC1.reshape((105,96))
             BC1d=BC1r.reshape((10080))
             cbeBC1 = BC1d[333:1666]
             BC2 =  fh.variables['BC2'][:]
             BC2=BC2[:,0]
             BC2r=BC2.reshape((105,96))
             BC2d=BC2r.reshape((10080))
             cbeBC2 = BC2d[333:1666]
             OC1 =  fh.variables['OC1'][:]
             OC1=OC1[:,0]
             OC1r=OC1.reshape((105,96))
             OC1d=OC1r.reshape((10080))
             cbeOC1 = OC1d[333:1666]
             OC2 =  fh.variables['OC2'][:]
             OC2=OC2[:,0]
             OC2r=OC2.reshape((105,96))
             OC2d=OC2r.reshape((10080))
             cbeOC2 = OC2d[333:1666]
             DUST_1 =  fh.variables['DUST_1'][:]
             DUST_1=DUST_1[:,0]
             DUST_1r=DUST_1.reshape((105,96))
             DUST_1d=DUST_1r.reshape((10080))
             cbeD1 = DUST_1d[333:1666]       
             DUST_2 =  fh.variables['DUST_2'][:]
             DUST_2=DUST_2[:,0]
             DUST_2r=DUST_2.reshape((105,96))
             DUST_2d=DUST_2r.reshape((10080))
             cbeD2 = DUST_2d[333:1666] 
             DUST_3 =  fh.variables['DUST_3'][:]
             DUST_3=DUST_3[:,0]
             DUST_3r=DUST_3.reshape((105,96))
             DUST_3d=DUST_3r.reshape((10080))
             cbeD3 = DUST_3d[333:1666]
             DUST_4 =  fh.variables['DUST_4'][:]
             DUST_4=DUST_4[:,0]
             DUST_4r=DUST_4.reshape((105,96))
             DUST_4d=DUST_4r.reshape((10080))
             cbeD4 = DUST_4d[333:1666]
             SEAS_1 =  fh.variables['SEAS_1'][:]
             SEAS_1=SEAS_1[:,0]
             SEAS_1r=SEAS_1.reshape((105,96))
             SEAS_1d=SEAS_1r.reshape((10080))
             cbeSS1 = SEAS_1d[333:1666]
             SEAS_2 =  fh.variables['SEAS_2'][:]
             SEAS_2=SEAS_2[:,0]
             SEAS_2r=SEAS_2.reshape((105,96))
             SEAS_2d=SEAS_2r.reshape((10080))
             cbeSS2 = SEAS_2d[333:1666]
             SEAS_3 =  fh.variables['SEAS_3'][:]
             SEAS_3=SEAS_3[:,0]
             SEAS_3r=SEAS_3.reshape((105,96))
             SEAS_3d=SEAS_3r.reshape((10080))
             cbeSS3 = SEAS_3d[333:1666]
             Temp =  fh.variables['T2'][:]
             Temp0=Temp.reshape((105,96))
             Temp1=Temp0.reshape((10080))
             cbeT = Temp1[333:1666]
             PSFC =  fh.variables['PSFC'][:]
             PSFC=PSFC.reshape((105,96))
             PSFC=PSFC.reshape((10080))
             cbePSFC = PSFC[333:1666]
             a=287.05*cbeT
             pd= cbePSFC/a
             P25 =  fh.variables['P25'][:]
             P25=P25[:,0]
             P25=P25.reshape((105,96))
             P25=P25.reshape((10080))
             cbeP25 = P25[333:1666]
             sulf =  fh.variables['sulf'][:]
             sulf=sulf[:,0]
             sulf=sulf.reshape((105,96))
             sulf=sulf.reshape((10080))
             cbeS = sulf[333:1666]
             PM25= pd*(cbeP25+1.375*cbeS+cbeBC1+cbeBC2+1.8*(cbeOC1+cbeOC2)+cbeD1+0.286*cbeD2+cbeSS1+0.0942*cbeSS2)
             PM10= pd*(cbeP25+(1.375*cbeS)+cbeBC1+cbeBC2+(1.8*(cbeOC1+cbeOC2))+cbeD1+cbeD2+cbeD3+(0.87*cbeD4)+cbeSS1+cbeSS2+cbeSS3)
     return PM25, PM10

pm251,pm101=ncwopandas()

# the earlier attempt #3 itself is working, actually it is miss match of module name and running of module

#attempt 5 for reading wrfpost nc file and gets its variables
def ncwppandas():
     wp=folreadwrfpost()
     time,T,RH,WS,WD=[],[],[],[],[]
     for i in wp:
             fh = Dataset(i, mode='r')
             tm1=fh.variables['DateTime'][:]
	     tm2=np.repeat(tm1, 1333)
	     temp = fh.variables['T_2m'][:]
             Temp0=temp.reshape((105,96))
             Temp1=Temp0.reshape((10080))
             cbeT = Temp1[333:1666]
             hum = fh.variables['rh_2m'][:]
             hum0=hum.reshape((105,96))
             hum1=hum0.reshape((10080))
             cbeRH = hum1[333:1666]
             ws = fh.variables['ws_10m'][:]
             ws0=ws.reshape((105,96))
             ws1=ws0.reshape((10080))
             cbeWS = ws1[333:1666]
             wd = fh.variables['wd_10m'][:]
             wd0=wd.reshape((105,96))
             wd1=wd0.reshape((10080))
             cbeWD = wd1[333:1666]
	     time.append(tm2)
             T.append(cbeT)
             RH.append(cbeRH)
	     WS.append(cbeWS)
	     WD.append(cbeWD)
     return time,T,RH,WS,WD

 
time1,T1,RH1,WS1,WD1=ncwppandas()

#attempt 6 to test the list from modules into numpy array then stack, then convert into pandas dataframe with correct date time index
#a test on array join based on [this](http://stackoverflow.com/questions/16473042/numpy-vstack-vs-column-stack)
#make a new array based on time index base on [this](http://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html)
time2=np.array(time1)
T12=np.array(T1)
a=time2[0]
d=np.repeat(a, 1333)
db=np.vstack((d,T12))
db2=pd.DataFrame(db)
db2.to_csv('DataA5.csv')
#attempt 7 to use the last test into a module
def nparcsv():
	a=[]
	time1,T1,RH1,WS1,WD1=ncwppandas()
	a=['T1','RH1','WS1','WD1']
	time2=np.array(time1)
	for i in range(4):
              a=time2[i]
	      d=np.repeat(a, 1333)
	      for b in a:
		  b=np.array(b)
                  db=np.hstack((d,b))	
		  db2=pd.DataFrame(db)
	db2.to_csv('DataA7.csv')

# this attempt not giving result, the csv file gerated contains only the date value and nothing else
#attempt 8 to test to get a numpy array from time array
def nparcsv():
	time1,T1,RH1,WS1,WD1=ncwppandas()
	time2=np.array(time1)
	var=['T1','RH1','WS1','WD1']
	theta_Matrix = []
	for i in range(4):
#this rnge has to be changed other wise erronoues in six hour simualtion
              a=time2[i]
	      d=np.repeat(a, 1333)
	      theta_Matrix.append(d)
        time3=np.array(theta_Matrix)
        for b in var:
	    db0=np.array(b)
            db=np.vstack((time3,db0))	
	db2=pd.DataFrame(db)
	db2.to_csv('DataA8.csv')


time1,T1,RH1,WS1,WD1=ncwppandas()
time2=np.array(time1)
theta_Matrix = []
for i in range(4):
      a=time2[i]
      d=np.repeat(a, 1333)
      theta_Matrix.append(d)        

# above attempt doen't end correctly or produnce what we want
#made a search for join structured array foun [this](http://stackoverflow.com/questions/5355744/numpy-joining-structured-arrays)
#attempt9
a1 = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('x', int), ('y', int)])
a2 = np.array([(7,10), (8,11), (9,12)], dtype=[('z', int), ('w', float)])
arrays = [a1, a2]     
import numpy.lib.recfunctions as rfn
rfn.merge_arrays(arrays, flatten = True, usemask = False)
array([(1, 2, 7, 10.0), (3, 4, 8, 11.0), (5, 6, 9, 12.0)], 
      dtype=[('x', '<i8'), ('y', '<i8'), ('z', '<i8'), ('w', '<f8')])
#looks promising and lets go forward for 
#attempt 10, based on abopve trail
def ncwppandas():
     wp=folreadwrfpost()
     time,T,RH,WS,WD=[],[],[],[],[]
     for i in wp:
             fh = Dataset(i, mode='r')
             tm1=fh.variables['DateTime'][:]
	     tm2=np.repeat(tm1, 1333)
	     temp = fh.variables['T_2m'][:]
             Temp0=temp.reshape((105,96))
             Temp1=Temp0.reshape((10080))
             cbeT = Temp1[333:1666]
             hum = fh.variables['rh_2m'][:]
             hum0=hum.reshape((105,96))
             hum1=hum0.reshape((10080))
             cbeRH = hum1[333:1666]
             ws = fh.variables['ws_10m'][:]
             ws0=ws.reshape((105,96))
             ws1=ws0.reshape((10080))
             cbeWS = ws1[333:1666]
             wd = fh.variables['wd_10m'][:]
             wd0=wd.reshape((105,96))
             wd1=wd0.reshape((10080))
             cbeWD = wd1[333:1666]
	     time.append(tm2)
             T.append(cbeT)
             RH.append(cbeRH)
	     WS.append(cbeWS)
	     WD.append(cbeWD)
     return time,T,RH,WS,WD

 
time2,T1,RH1,WS1,WD1=ncwppandas()
arrays = [time1,T1,RH1,WS1,WD1]  
adt=rfn.merge_arrays(arrays, flatten = True, usemask = False)
adt1=pd.DataFrame(adt)
adt1.to_csv('DATA9.csv')
#it is done now the data frame is created as we want great link monumenta is [this](http://stackoverflow.com/questions/5355744/numpy-joining-structured-arrays), saved more than three hour search
#attempt 11, joining the wrf output and wrfpost numpy arrays
time1,lat1,lon1,pm251,pm101=ncwopandas()
time2,T1,RH1,WS1,WD1=ncwppandas()
arrays = [time1,time2,lat1,lon1,T1,RH1,WS1,WD1,pm251,pm101]  
adt=rfn.merge_arrays(arrays, flatten = True, usemask = False)
adt1=pd.DataFrame(adt)
adt1.to_csv('DATA10.csv')
#with this the attempt to convert wrf output into numpy array then into pandas then into csv is over

