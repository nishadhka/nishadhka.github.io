#!/usr/bin/python
import serial
import time
import sqlite3 as lite
import logging
import subprocess
import re

logger = logging.getLogger('lbm1')
hdlr = logging.FileHandler('/home/pi/SMS/data.log')
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info("cronjob started")

ser = serial.Serial('/dev/dylos', 9600, timeout=60)
try:
   with ser:
       	time.sleep(60)
       	line = ser.readline()
	now = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        a =  "%s,%s" % (now,line)
        #print a
        b = a.strip(' \00/r/n')
       
except:
        logger.exception('serial not ready')
finally:
    if ser:
       ser.close()

var = 1
while var ==1:
   output = subprocess.check_output(["./Adafruit_DHT", "11", "4"]);
   matches = re.search("Temp =\s+([0-9.]+)", output)
   if (not matches):
         time.sleep(3)
         continue
   temp = float(matches.group(1))
   matches = re.search("Hum =\s+([0-9.]+)", output)
   if (not matches):
         time.sleep(3)
         continue
   humidity = float(matches.group(1))
   break  

tempS = str(temp)
HumS = str(humidity)


con = lite.connect('/home/pi/SMS/dylos.db')
try:
   with con:
       cur = con.cursor()
       cur.execute("INSERT INTO data(data,TEMP,HUMP) VALUES(?,?,?)", (b,tempS,HumS))
       logger.info("data saved in db")
except:
        logger.exception('database yet to ready')
finally:
    if con:
       con.close() 
logger.info("cronjob over")
