from netCDF4 import Dataset
import numpy as np
import pandas
import itertools
import utm
import os
import re

path = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/'
ncf = [f for f in os.listdir(path) if f.endswith('.nc')]
var=[]
for i in ncf:
    var.append(re.findall(r'Asia_(.*?)_2010', i))
    break


# opening a single netcdf for get lat long values in it
my_example_nc_file = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/MICS_Asia_PM10_2010_0.25x0.25.nc'
fh = Dataset(my_example_nc_file, mode='r')
lons = fh.variables['lon'][:]
count0=np.arange(40.125,73.125,0.25)
count1=np.arange(73.125,82.125,0.25)
slo=len(count0)
dlo=len(count1)
elo=slo+dlo
cbeDom2lon = fh.variables['lon'][slo:elo]
lats = fh.variables['lat'][:]
count0=np.arange(-20.125,8.125,0.25)
count1=np.arange(8.125,16.125,0.25)
sla=len(count0)
dla=len(count1)
ela=sla+dla
cbeDom2lat = fh.variables['lat'][sla:ela]
a=list(itertools.product(cbeDom2lon,cbeDom2lat))
a1=pandas.DataFrame(a)
b=[]
for i in a:
	c=utm.from_latlon(i[1],i[0])
	b.append(c)
b1=pandas.DataFrame(b)

#Doing netcdf subset 
f = open(data_A1.csv, 'a')
data = pandas.DataFrame()
pct = []
for i in ncf:
    fh = Dataset(i, mode='r')
    var = re.findall(r'Asia_(.*?)_2010', i)
    print fh.variables.keys()
    for m in range(12):
    	###for loop for months
    	pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
	pm10ri = np.ravel(pm10r)
    	pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
    	pm10ii = np.ravel(pm10i)
    	pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
    	pm10pi = np.ravel(pm10p)
    	pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
    	pm10ti = np.ravel(pm10t)
    	c1=pandas.DataFrame(pm10ri)
    	c2=pandas.DataFrame(pm10ii)
    	c3=pandas.DataFrame(pm10pi)
    	c4=pandas.DataFrame(pm10ti)
    	c5=c1+c2+c3+c4
    	c5.columns = [str(var[0])+'_'+str(m)]
        pct.append(c5)
X = np.array(pct)
        #c5.append(data)
        #d1=pandas.merge([data,c5])
        #d1=pandas.concat([data,c5],axis=1)
    	#c5.to_csv(str(var[0])+'_month_'+str(m)+'.csv', mode='a', header=False)
        #c5.to_csv(f, header = False)
        #d1.to_csv('data'+str(var[0]+'.csv')



pct = []
for i in ncf:
    fh = Dataset(i, mode='r')
    var = re.findall(r'Asia_(.*?)_2010', i)
    print fh.variables.keys()
    for m in range(12):
    	###for loop for months
    	pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
	pm10ri = np.ravel(pm10r)
    	pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
    	pm10ii = np.ravel(pm10i)
    	pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
    	pm10pi = np.ravel(pm10p)
    	pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
    	pm10ti = np.ravel(pm10t)
    	c3=np.column_stack((pm10ri,pm10ii,pm10pi,pm10ti))
        c4=c3.sum(axis=1)
        c5=np.array(c4,dtype=[(str(var[0])+'_'+str(m),'<f8')])
        #c5=pandas.DataFrame(pm10ti)
    	#c5.columns = [str(var[0])+'_'+str(m)]
        pct.append(c5)

data=pandas.DataFrame(pct)
data2=pandas.DataFrame.transpose(data)
var=pandas.DataFrame.from_csv('variables.csv', header=0, index_col=[0])
varL=var['variables'].tolist()
data2.columns=varL
aV=['long','lat']
uV=['X','Y','Zone','a']
a1.columns=aV
b1.columns=uV
data3=pandas.concat([a1,b1,data2],axis=1)
data3.ix[:5, :10]
MICS_m1=data3[['long','lat','X','Y','CO_0', 'BC_0', 'NMVOC_0', 'NOx_0', 'PM10_0', 'PM2.5_0', 'CO2_0', 'SO2_0', 'OC_0', 'NH3_0']]
MICS_m1.to_csv('MICS_2010_m01.csv')
MICS_m1=data3[['long','lat','X','Y','CO_1', 'BC_1', 'NMVOC_1', 'NOx_1', 'PM10_1', 'PM2.5_1', 'CO2_1', 'SO2_1', 'OC_1', 'NH3_1']]
MICS_m1.to_csv('MICS_2010_m02.csv')
MICS_m1=data3[['long','lat','X','Y','CO_2', 'BC_2', 'NMVOC_2', 'NOx_2', 'PM10_2', 'PM2.5_2', 'CO2_2', 'SO2_2', 'OC_2', 'NH3_2']]
MICS_m1.to_csv('MICS_2010_m03.csv')
MICS_m1=data3[['long','lat','X','Y','CO_3', 'BC_3', 'NMVOC_3', 'NOx_3', 'PM10_3', 'PM2.5_3', 'CO2_3', 'SO2_3', 'OC_3', 'NH3_3']]
MICS_m1.to_csv('MICS_2010_m04.csv')
MICS_m1=data3[['long','lat','X','Y','CO_4', 'BC_4', 'NMVOC_4', 'NOx_4', 'PM10_4', 'PM2.5_4', 'CO2_4', 'SO2_4', 'OC_4', 'NH3_4']]
MICS_m1.to_csv('MICS_2010_m05.csv')
MICS_m1=data3[['long','lat','X','Y','CO_5', 'BC_5', 'NMVOC_5', 'NOx_5', 'PM10_5', 'PM2.5_5', 'CO2_5', 'SO2_5', 'OC_5', 'NH3_5']]
MICS_m1.to_csv('MICS_2010_m06.csv')
MICS_m1=data3[['long','lat','X','Y','CO_6', 'BC_6', 'NMVOC_6', 'NOx_6', 'PM10_6', 'PM2.5_6', 'CO2_6', 'SO2_6', 'OC_6', 'NH3_6']]
MICS_m1.to_csv('MICS_2010_m07.csv')
MICS_m1=data3[['long','lat','X','Y','CO_7', 'BC_7', 'NMVOC_7', 'NOx_7', 'PM10_7', 'PM2.5_7', 'CO2_7', 'SO2_7', 'OC_7', 'NH3_7']]
MICS_m1.to_csv('MICS_2010_m08.csv')
MICS_m1=data3[['long','lat','X','Y','CO_8', 'BC_8', 'NMVOC_8', 'NOx_8', 'PM10_8', 'PM2.5_8', 'CO2_8', 'SO2_8', 'OC_8', 'NH3_8']]
MICS_m1.to_csv('MICS_2010_m09.csv')
MICS_m1=data3[['long','lat','X','Y','CO_9', 'BC_9', 'NMVOC_9', 'NOx_9', 'PM10_9', 'PM2.5_9', 'CO2_9', 'SO2_9', 'OC_9', 'NH3_9']]
MICS_m1.to_csv('MICS_2010_m10.csv')
MICS_m1=data3[['long','lat','X','Y','CO_10', 'BC_10', 'NMVOC_10', 'NOx_10', 'PM10_10', 'PM2.5_10', 'CO2_10', 'SO2_10', 'OC_10', 'NH3_10']]
MICS_m1.to_csv('MICS_2010_m11.csv')
MICS_m1=data3[['long','lat','X','Y','CO_11', 'BC_11', 'NMVOC_11', 'NOx_11', 'PM10_11', 'PM2.5_11', 'CO2_11', 'SO2_11', 'OC_11', 'NH3_11']]
MICS_m1.to_csv('MICS_2010_m12.csv')

 





X=np.asarray(pct,'<f8')





pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
pm10ri = np.ravel(pm10r)
pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
pm10ii = np.ravel(pm10i)
pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
pm10pi = np.ravel(pm10p)
pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
pm10ti = np.ravel(pm10t)
c3=np.column_stack((pm10ri,pm10ii,pm10pi,pm10ti))
c4=c3.sum(axis=1)
c5=np.array(c4,dtype=[(str(var[0])+'_'+str(m),'float')])


a = np.array([]).reshape(120,1152)





pct = np.array([])
def myfunc():
	for i in ncf:
    		fh = Dataset(i, mode='r')
    		var = re.findall(r'Asia_(.*?)_2010', i)
    		print fh.variables.keys()
    		for m in range(12):
    	###for loop for months
    			pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
			pm10ri = np.ravel(pm10r)
		    	pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
		    	pm10ii = np.ravel(pm10i)
		    	pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
		    	pm10pi = np.ravel(pm10p)
		    	pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
		    	pm10ti = np.ravel(pm10t)
		    	c3=np.column_stack((pm10ri,pm10ii,pm10pi,pm10ti))
		        c4=c3.sum(axis=1)
		        c5=np.array(c4,dtype=[(str(var[0])+'_'+str(m),'float')])
        #c5=pandas.DataFrame(pm10ti)
    	#c5.columns = [str(var[0])+'_'+str(m)]
        #pct=np.c_[pct, [[c5]]]
        pct = np.append(pct, [c5], axis=1)
X = np.array(pct)








strs = ["CO_" for x in range(12)]
e=np.array(strs)
c=np.arange(0,12,1)
c2=pandas.DataFrame(c)
c3=pandas.DataFrame(e)
c4 = c3[0].str.cat(c2[0].values.astype(str), sep=' is ')
c4 = c3.map(str) + " is " + c2



np.column_stack((a,b))



               ^
IndentationError: unindent does not match any outer indentation level




Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: can only concatenate list (not "str") to list




ptt=np.add(pm10ri, pm10ii, pm10pi, pm10ti)
	k='row%d'%(i,)
	l[k] = ptt

	












c1=pandas.DataFrame(pm10ri)
	c2=pandas.DataFrame(pm10ii)
	c3=pandas.DataFrame(pm10pi)
	c4=pandas.DataFrame(pm10ti)
	c5=c1+c2+c3+c4

	d1=pandas.concat([a1,b1,c1],axis=1)
	d1.to_csv(var[0]+'.csv')





my_example_nc_file = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/MICS_Asia_PM10_2010_0.25x0.25.nc'
fh = Dataset(my_example_nc_file, mode='r')
lons = fh.variables['lon'][:]
count0=np.arange(40.125,72.625,0.25)
count1=np.arange(72.625,85.375,0.25)
slo=len(count0)
dlo=len(count1)
elo=slo+dlo
dY=elo-slo
cbeDom2lon = fh.variables['lon'][slo:elo]
lats = fh.variables['lat'][:]
count0=np.arange(-20.125,5.125,0.25)
count1=np.arange(5.125,22.875,0.25)
sla=len(count0)
dla=len(count1)
ela=sla+dla
dY=ela-sla
cbeDom2lat = fh.variables['lat'][sla:ela]
a=list(itertools.product(cbeDom2lon,cbeDom2lat))
a1=pandas.DataFrame(a)
b=[]
for i in a:
	c=utm.from_latlon(i[1],i[0])
	b.append(c)
b1=pandas.DataFrame(b)
path = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/'
ncf = [f for f in os.listdir(path) if f.endswith('.nc')]
var_name=[]
pct = []
for i in ncf:
    fh = Dataset(i, mode='r')
    var = re.findall(r'Asia_(.*?)_2010', i)
    print fh.variables.keys()
    for m in range(12):
    	###for loop for months
    	pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
	pm10ri = np.ravel(pm10r)
    	pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
    	pm10ii = np.ravel(pm10i)
    	pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
    	pm10pi = np.ravel(pm10p)
    	pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
    	pm10ti = np.ravel(pm10t)
    	c3=np.column_stack((pm10ri,pm10ii,pm10pi,pm10ti))
        c4=c3.sum(axis=1)
        c5=np.array(c4,dtype=[(str(var[0])+'_'+str(m),'<f8')])
        #c5=pandas.DataFrame(pm10ti)
    	#c5.columns = [str(var[0])+'_'+str(m)]
        pct.append(c4)
        var_name.append(c5)
data=pandas.DataFrame(pct)
data2=pandas.DataFrame.transpose(data)
var=pandas.DataFrame.from_csv('variables.csv', header=0, index_col=[0])
# above step is a ju, can't able to get column list form structure list pct
varL=var['variables'].tolist()
data2.columns=varL
aV=['long','lat']
uV=['X','Y','Zone','a']
a1.columns=aV
b1.columns=uV
data3=pandas.concat([a1,b1,data2],axis=1)
data3.ix[:5, :10]
MICS_m1=data3[['long','lat','X','Y','CO_0', 'BC_0', 'NMVOC_0', 'NOx_0', 'PM10_0', 'PM2.5_0', 'CO2_0', 'SO2_0', 'OC_0', 'NH3_0']]
MICS_m1['CO_0_c']=(MICS_m1.CO_0*(1000000/731.484))/28.01
MICS_m1['NH3_0_c']=(MICS_m1.NH3_0*(1000000/731.484))/17.031
MICS_m1['SO2_0_c']=(MICS_m1.SO2_0*(1000000/731.484))/64.066
MICS_m1['PM25_0_c']=MICS_m1['PM2.5_0']*(1000000/731.484)
MICS_m1['PM10_0_c']=MICS_m1.PM10_0*(1000000/731.484)
MICS_m1.to_csv('MICS_2010_D01D04_m01.csv')
MICS_m1=data3[['long','lat','X','Y','CO_1', 'BC_1', 'NMVOC_1', 'NOx_1', 'PM10_1', 'PM2.5_1', 'CO2_1', 'SO2_1', 'OC_1', 'NH3_1']]
MICS_m1.to_csv('MICS_2010_D01D04_m02.csv')
MICS_m1=data3[['long','lat','X','Y','CO_2', 'BC_2', 'NMVOC_2', 'NOx_2', 'PM10_2', 'PM2.5_2', 'CO2_2', 'SO2_2', 'OC_2', 'NH3_2']]
MICS_m1.to_csv('MICS_2010_D01D04_m03.csv')
MICS_m1=data3[['long','lat','X','Y','CO_3', 'BC_3', 'NMVOC_3', 'NOx_3', 'PM10_3', 'PM2.5_3', 'CO2_3', 'SO2_3', 'OC_3', 'NH3_3']]
MICS_m1.to_csv('MICS_2010_D01D04_m04.csv')
MICS_m1=data3[['long','lat','X','Y','CO_4', 'BC_4', 'NMVOC_4', 'NOx_4', 'PM10_4', 'PM2.5_4', 'CO2_4', 'SO2_4', 'OC_4', 'NH3_4']]
MICS_m1.to_csv('MICS_2010_D01D04_m05.csv')
MICS_m1=data3[['long','lat','X','Y','CO_5', 'BC_5', 'NMVOC_5', 'NOx_5', 'PM10_5', 'PM2.5_5', 'CO2_5', 'SO2_5', 'OC_5', 'NH3_5']]
MICS_m1.to_csv('MICS_2010_D01D04_m06.csv')
MICS_m1=data3[['long','lat','X','Y','CO_6', 'BC_6', 'NMVOC_6', 'NOx_6', 'PM10_6', 'PM2.5_6', 'CO2_6', 'SO2_6', 'OC_6', 'NH3_6']]
MICS_m1.to_csv('MICS_2010_D01D04_m07.csv')
MICS_m1=data3[['long','lat','X','Y','CO_7', 'BC_7', 'NMVOC_7', 'NOx_7', 'PM10_7', 'PM2.5_7', 'CO2_7', 'SO2_7', 'OC_7', 'NH3_7']]
MICS_m1.to_csv('MICS_2010_D01D04_m08.csv')
MICS_m1=data3[['long','lat','X','Y','CO_8', 'BC_8', 'NMVOC_8', 'NOx_8', 'PM10_8', 'PM2.5_8', 'CO2_8', 'SO2_8', 'OC_8', 'NH3_8']]
MICS_m1.to_csv('MICS_2010_D01D04_m09.csv')
MICS_m1=data3[['long','lat','X','Y','CO_9', 'BC_9', 'NMVOC_9', 'NOx_9', 'PM10_9', 'PM2.5_9', 'CO2_9', 'SO2_9', 'OC_9', 'NH3_9']]
MICS_m1.to_csv('MICS_2010_D01D04_m10.csv')
MICS_m1=data3[['long','lat','X','Y','CO_10', 'BC_10', 'NMVOC_10', 'NOx_10', 'PM10_10', 'PM2.5_10', 'CO2_10', 'SO2_10', 'OC_10', 'NH3_10']]
MICS_m1.to_csv('MICS_2010_D01D04_m11.csv')
MICS_m1=data3[['long','lat','X','Y','CO_11', 'BC_11', 'NMVOC_11', 'NOx_11', 'PM10_11', 'PM2.5_11', 'CO2_11', 'SO2_11', 'OC_11', 'NH3_11']]
MICS_m1.to_csv('MICS_2010_D01D04_m12.csv')



from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrfchemi_d01_5A'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfchemi_d01_5A.csv')


from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrfchemi_d01_4A'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfchemi_d01_4A.csv')


from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrfchemi_gocart_bg_d01_4A'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfchemi_gocart_bg_d01_4A.csv')


from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrffirechemi_d01_4A'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrffirechemi_d01_4A.csv')


my_example_nc_file = 'wrfbdy_d01'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfbdy_d01.csv')


my_example_nc_file = 'wrfinput_d01'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfinput_d01.csv')


f = h5py.File('EDGAR_2005.h5','r')
f.keys()
f['AVIATION_SOURCES']
f['AVIATION_SOURCES'].keys()
f['AVIATION_SOURCES']['CO']
store = pandas.HDFStore('EDGAR_2005.h5','r')
store.keys()
store



from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrfem_00to12z_d01'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()



import fortranfile
f = fortranfile.FortranFile('wrfem_00to12z_d01')
x = f.readReals()




#SINce the pywrf emiss not interoplating data for domin 01. It is decided to make larger domain fitting the CBE_d01 and rerun the program. Below code is in that direction with changes for lat and log covering cbe_d01.
from netCDF4 import Dataset
import numpy as np
import pandas
import itertools
import utm
import os
import re
my_example_nc_file = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/MICS_Asia_PM10_2010_0.25x0.25.nc'
fh = Dataset(my_example_nc_file, mode='r')
lons = fh.variables['lon'][:]
count0=np.arange(40.125,65.125,0.25)
count1=np.arange(65.125,90.375,0.25)
slo=len(count0)
dlo=len(count1)
elo=slo+dlo
cbeDom2lon = fh.variables['lon'][slo:elo]
lats = fh.variables['lat'][:]
count0=np.arange(-20.125,5.125,0.25)
count1=np.arange(5.125,30.875,0.25)
sla=len(count0)
dla=len(count1)
ela=sla+dla
cbeDom2lat = fh.variables['lat'][sla:ela]
a=list(itertools.product(cbeDom2lon,cbeDom2lat))
a1=pandas.DataFrame(a)
b=[]
for i in a:
	c=utm.from_latlon(i[1],i[0])
	b.append(c)
b1=pandas.DataFrame(b)
path = '/home/swl-sacon-dst/Documents/GISE_2013/LAB/WRF-chem/Data/2010/'
ncf = [f for f in os.listdir(path) if f.endswith('.nc')]
var_name=[]
pct = []
for i in ncf:
    fh = Dataset(i, mode='r')
    var = re.findall(r'Asia_(.*?)_2010', i)
    print fh.variables.keys()
    for m in range(12):
    	###for loop for months
    	pm10r = fh.variables[str(var[0])+'_RESIDENTIAL'][m,slo:elo,sla:ela]
	pm10ri = np.ravel(pm10r)
    	pm10i = fh.variables[str(var[0])+'_INDUSTRY'][m,slo:elo,sla:ela]
    	pm10ii = np.ravel(pm10i)
    	pm10p = fh.variables[str(var[0])+'_POWER'][m,slo:elo,sla:ela]
    	pm10pi = np.ravel(pm10p)
    	pm10t = fh.variables[str(var[0])+'_TRANSPORT'][m,slo:elo,sla:ela]
    	pm10ti = np.ravel(pm10t)
    	c3=np.column_stack((pm10ri,pm10ii,pm10pi,pm10ti))
        c4=c3.sum(axis=1)
        c5=np.array(c4,dtype=[(str(var[0])+'_'+str(m),'<f8')])
        #c5=pandas.DataFrame(pm10ti)
    	#c5.columns = [str(var[0])+'_'+str(m)]
        pct.append(c4)
        var_name.append(c5)
data=pandas.DataFrame(pct)
data2=pandas.DataFrame.transpose(data)
var=pandas.DataFrame.from_csv('variables.csv', header=0, index_col=[0])
# above step is a ju, can't able to get column list form structure list pct
varL=var['variables'].tolist()
data2.columns=varL
aV=['long','lat']
uV=['X','Y','Zone','a']
a1.columns=aV
b1.columns=uV
data3=pandas.concat([a1,b1,data2],axis=1)
data3.ix[:5, :10]
MICS_m1=data3[['long','lat','X','Y','CO_0', 'BC_0', 'NMVOC_0', 'NOx_0', 'PM10_0', 'PM2.5_0', 'CO2_0', 'SO2_0', 'OC_0', 'NH3_0']]
MICS_m1['CO_0_c']=(MICS_m1.CO_0*(1000000/731.484))/28.01
MICS_m1['NH3_0_c']=(MICS_m1.NH3_0*(1000000/731.484))/17.031
MICS_m1['SO2_0_c']=(MICS_m1.SO2_0*(1000000/731.484))/64.066
MICS_m1['PM25_0_c']=MICS_m1['PM2.5_0']*(1000000/731.484)
MICS_m1['PM10_0_c']=MICS_m1.PM10_0*(1000000/731.484)
MICS_m1.to_csv('MICS_2010_D01D04_m01_DO1.csv')


from netCDF4 import Dataset
import numpy as np
import pandas
my_example_nc_file = 'wrfchemi_d01_6A'
fh = Dataset(my_example_nc_file, mode='r')
a1= fh.variables.keys()
a2=[]
for i in a1:
     print i
     a=fh.variables[i][:]
     aa = np.ravel(a)
     a2.append(aa)
data=pandas.DataFrame(a2)
data2=pandas.DataFrame.transpose(data)
col=pandas.DataFrame(a1)
varL=col[0].tolist()
data2.columns=varL
data2.to_csv('wrfchemi_d01_6A.csv')



