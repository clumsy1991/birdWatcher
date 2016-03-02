#! /usr/bin/python -B

###############################################################
########                birdWatcher.py                 ######## 
########             Made by Thomas Roberts            ######## 
########                  01/03/2016                   ########
###############################################################


import os
import sys
import logging
import time
import datetime
import subprocess
import RPi.GPIO as GPIO

# Define for log file
logFile="/var/log/birdWatcher.log"

# GPIO for PIR
PIR = 4



def getFileName():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")


def takePhoto():
	for i in range(1,2):
		capturename = getFileName()
		logging.info("Motion detected! Taking snapshot %s", capturename)
		cmd="raspistill -w 640 -h 480 -n -t 10 -q 10 -e jpg -th none -o /home/pi/" + capturename+"_%d.jpg" % (i)
		camerapid = subprocess.call(cmd,shell=True)

if __name__ == "__main__":
	# Initialise all logging configuration, only levels equal to info or above will be logged, the stream will be stdout and message will appear as the following:
	# DEBUG: This is DEBUG (only if configured)
	# INFO: This is information
	# Warning: This is a warning
	# Error: This is a error
	logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(levelname)s: %(message)s')
	run = True
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)

	logging.info("Turning on PIR motion sensor")
	
	while GPIO.input(PIR) == 1:
		currentSate = 0

	logging.info("PIR Sensor is Ready")

	while run == True:
		logging.debug("Waiting for movement...")
		GPIO.wait_for_edge(PIR, GPIO.RISING)
		takePhoto()

