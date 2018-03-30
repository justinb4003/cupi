#!/usr/bin/python
# Copyright Justin Buist

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import time
import socket

from threading import Thread

s = socket.socket()
s.bind(('', 2048))
s.listen(5)

keepRunning = True

def getNetCommand():
    global keepRunning
    while keepRunning:
        c, addr = s.accept()
        print 'Connection from:', addr
        retVal = c.recv(1024)
        print 'received:', retVal
        c.close()

sthread = Thread(name="server", target=getNetCommand)
sthread.setDaemon(True)
sthread.start()
while keepRunning:
    try:
        print 'Main thread...'
        time.sleep(1.00)
    except KeyboardInterrupt:
        print 'Bye!'
        keepRunning = False
