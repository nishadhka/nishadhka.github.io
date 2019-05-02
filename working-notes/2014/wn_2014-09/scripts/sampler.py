#! /usr/bin/python

#The MIT License (MIT)
# A script to manage Dylos air quality monitor and Aerocet 531S, colocated sampling for calibration of dylos to get reading in ug/m3
# (C)2014 Nishadh K A <nishadhka@gmail.com>
# Requiers miniterm.py from http://cs.earlham.edu/~charliep/ecoi/serial/pyserial-2.2/examples/miniterm.py


import pexpect
import itertools
import time 
import serial
from threading import Thread

def a531s():
        csv_file= open('/home/pi/aerocet/a531s.csv','a')
	command = "python miniterm3.py -p '/dev/ttyUSB1' -b 9600"
	child=pexpect.spawn(command)
        #For Count mode
        for _ in itertools.repeat(None, 5):
	    child.sendline ('')
	child.sendline ('MM 0')
        child.sendline ('S')
        # here have to wait for 60 seconds to finish the sampling
        time.sleep(61)
	for _ in itertools.repeat(None, 8):
            child.sendline ('')
        cto = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        #For Mass mode
        for _ in itertools.repeat(None, 5):
	    child.sendline ('')
	child.sendline ('MM 1')
	child.sendline ('S')
        time.sleep(61)
        mao = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
	for _ in itertools.repeat(None, 9):
	    child.sendline ('')
        a =  "%s,%s" % (cto,mao)
        csv_file.write(a)
        csv_file.flush()
        csv_file.close()
	child.close()

def dylos():
        csv_file= open('/home/pi/aerocet/dylos.csv','a')
	ser = serial.Serial('/dev/dylos', 9600, timeout=60)
	try:
   		with ser:
       			time.sleep(60)
       			line = ser.readline()
			now = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
		        a =  "%s,%s" % (now,line)
		        #print a
		        b = a.strip(' \00/r/n')
			print b
		        csv_file.write(b)
		        csv_file.flush()
		        csv_file.close()
       
	except:
		print'serial not ready'
	finally:
	    if ser:
	       ser.close()


      	
#a531s()
#dylos()
if __name__ == '__main__':
    Thread(target = a531s).start()
    Thread(target = dylos).start()

