#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# led_on.py
# Turn on a led 
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO    
import time				

GPIO.setmode(GPIO.BOARD)  
LED_PIN = 12		
GPIO.setup(LED_PIN, GPIO.OUT)    

print("LED is on")
GPIO.output(LED_PIN, GPIO.HIGH)    
time.sleep(3)

GPIO.cleanup()   

