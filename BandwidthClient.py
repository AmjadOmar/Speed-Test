#!/usr/bin/python3

import sys, time
from socket import *

count = 1000
BUFSIZE = 2048000
ip=input("ip: ")
port=input("Port: ")
def client():
    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((ip, int(port)))
    t3 = time.time()
    i = 0
    while i < count:
        i = i+1
        s.send(bytearray(testdata,"utf-8"))
    s.shutdown(1)
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    print (data.decode())
    print ('ping:', (t3-t2)+(t5-t4)/2)
    print ('Time:', t4-t3)
    print ('Bandwidth:', round((BUFSIZE*count*0.001) / (t4-t3), 3),)
    print ('Kb/sec.')
client()
