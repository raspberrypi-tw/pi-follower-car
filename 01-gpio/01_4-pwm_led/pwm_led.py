#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# pwm_led.py
# Adjust the bright of a led by software PWM
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PWM_PIN = 12
GPIO.setup(PWM_PIN, GPIO.OUT)

pwm = GPIO.PWM(PWM_PIN, 500)
pwm.start(0)

try:
    while True:
        duty_s = raw_input("Enter Brightness (0 to 100):")
        duty = int(duty_s)

        if duty >= 0 and duty <=100 :
            pwm.ChangeDutyCycle(duty)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    pwm.stop()
    GPIO.cleanup()          
