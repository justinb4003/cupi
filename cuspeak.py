#!/usr/bin/python
# Copyright Countryside Greenhouse

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

RUN_ON_PI = False

SOUND_DIR="/home/jbuist/git/cupi/"

if RUN_ON_PI:
    import RPi.GPIO as GPIO
from pygame import mixer
from threading import Thread
import pygame
import socket
import time

if RUN_ON_PI:
    GPIO.setmode(GPIO.BCM)
    # Appearntly not needed for IO3.. go fig.
    #GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(3, GPIO.IN)
    GPIO.setup(5, GPIO.OUT)

def getSpeakButton():
    if RUN_ON_PI:
        status = GPIO.input(3)
    else:
        status = 1

    if status == 1:
        status = 0
    elif status == 0:
        status = 1
    return status

def playSoundFile(filename):
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def getNetCommand():
    global keepRunning
    while keepRunning:
        c, addr = s.accept()
        print 'Connection from:', addr
        retVal = c.recv(1024)
        print 'received:', retVal
        c.close()


keepRunning = True

s = socket.socket()
s.bind(('', 2048))
s.listen(5) # find out why 5... 
sthread = Thread(name="server", target=getNetCommand)
sthread.setDaemon(True)
sthread.start()

# Startup
pygame.init()
mixer.init()
playSoundFile(SOUND_DIR + "bootup.mp3")

while keepRunning:
    if RUN_ON_PI:
        GPIO.output(5, 0)
    status = getSpeakButton()
    #print status
    if status == 1:
        if RUN_ON_PI:
            GPIO.output(5, 1)
        playSoundFile("/opt/cside/bin/lawman_nocash_green_egg.mp3")






