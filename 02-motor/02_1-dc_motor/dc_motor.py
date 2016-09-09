#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# dc_motor.py
# control a dc motor to start rotating and stop rotating
#
# Author : sosorry
# Date   : 08/01/2015

import RPi.GPIO as GPIO
import time

MOTOR_PIN = 16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MOTOR_PIN, GPIO.OUT)

try:
    while True:
        print("Motor start ...")
        GPIO.output(MOTOR_PIN, GPIO.HIGH)
        time.sleep(2)

        print("Motor stop !!!")
        GPIO.output(MOTOR_PIN, GPIO.LOW)
        time.sleep(2)
finally:
    GPIO.cleanup()                            
