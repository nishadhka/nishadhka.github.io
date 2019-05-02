import sys, os, serial
#threading, getopt
import logging
EXITCHARCTER = '\x04'   #ctrl+D


logger = logging.getLogger('A531S')
hdlr = logging.FileHandler('mt4.log')
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info("serial started")

def getkey():
    c = 'S'
    return c


CONVERT_CRLF = 2
CONVERT_CR   = 1
CONVERT_LF   = 0

def reader():
    """loop forever and copy serial->console"""
    while 1:
        data = s.read()
        if repr_mode:
            sys.stdout.write(repr(data)[1:-1])
        else:
            sys.stdout.write(data)
        sys.stdout.flush()
        reads={'ser':data}
        return reads

def writer():
    """loop and copy console->serial until EOF character is found"""
    while 1:
        c = 'S\r\n'
        if c == EXITCHARCTER: 
            break                       #exit app
        elif c == '\n':
            if convert_outgoing == CONVERT_CRLF:
                s.write('\r\n')         #make it a CR+LF
            elif convert_outgoing == CONVERT_CR:
                s.write('\r')           #make it a CR
            elif convert_outgoing == CONVERT_LF:
                s.write('\n')           #make it a LF
        else:
            s.write(c)                  #send character


port  = '/dev/ttyUSB2'
baudrate = 9600
    
try:
    s = serial.Serial(port, baudrate)
except:
    logger.exception('serial not ready')
#start serial->console thread
#r = threading.Thread(target=reader)
#r.setDaemon(1)
#r.start()
#a=reader()
#print a['ser']
#and enter console->serial loop
writer()
