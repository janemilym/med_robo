#!/usr/bin/python
print "Content-type: text/html\n\n";

import serial
import time
import sys

#print("Moving Robot")
#print(len(sys.argv))

cmd = '#'+sys.argv[1]+'\r'

#print(cmd)

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.1)
ser.write(cmd)
time.sleep(.1)
ser.close()
