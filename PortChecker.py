#!/usr/bin/env python
'''
7/15/16 - Sean Lyngen

Python script running a tcp connect scan using socket against a list of
ip addresses from a text file.

User selects number of times to run the test and the time between tests

cls is used to clear the screen on a windows machine

'''
import socket
import re
import sys
import os
import time
sourcefile = raw_input('Enter full path of IP list file to Scan: ')
while os.path.exists(sourcefile) is False:
        sourcefile = raw_input("File doesn't exist, enter full path of IP list file to Scan: ")
destport = input('Enter TCP port to Scan: ')
iterations = input('How many times to run the test: ')
seconds = input('How many seconds between tests: ')
for i in range(iterations):
        target = open(sourcefile)
        for ip in target.readlines():
                s = socket.socket()
                host = ip.rstrip('\n')
                try:
                        s.connect((host, destport))
                        print "Connection to %s on tcp port %s successful" % (host, destport)            
                except socket.error, e:
                        print "Connection to %s on tcp port %s failed: Error %s" % (host, destport, e)
                s.close()
        time.sleep(seconds)
        target.close()
        os.system('cls')
