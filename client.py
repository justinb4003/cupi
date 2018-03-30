#!/usr/bin/python
# Copyright Justin Buist

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import socket

s = socket.socket()
s.connect(('127.0.0.1', 2048))
s.send('Hello, world!')
s.close()

