#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# l298n_motor.py
# control a dc motor clockwise and counterclockwise
#
# Author : sosorry
# Date   : 08/01/2015

import RPi.GPIO as GPIO
import time

Motor_R1_Pin = 16
Motor_R2_Pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT)
GPIO.setup(Motor_R2_Pin, GPIO.OUT)

try:
    GPIO.output(Motor_R1_Pin, True)     # clockwise
    time.sleep(3)
    GPIO.output(Motor_R1_Pin, False)

    time.sleep(1)                       # protect motor

    GPIO.output(Motor_R2_Pin, True)     # counterclockwise
    time.sleep(3)
    GPIO.output(Motor_R2_Pin, False)

finally:
    GPIO.cleanup()

