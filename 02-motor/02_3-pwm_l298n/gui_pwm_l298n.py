#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# gui_pwm_l298n.py
# control a dc motor with PWM
#
# Author : sosorry
# Date   : 08/30/2016
# Origin : https://github.com/simonmonk/raspberrypi_cookbook/blob/master/code/gui_slider.py

from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
pwm = GPIO.PWM(16, 500)
pwm.start(0)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=100,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))


root = Tk()
root.wm_title('PWM Power Control')

try:
    app = App(root)
    root.geometry("200x50+100+100")
    root.mainloop()

finally:
    pwm.stop()
    GPIO.cleanup()

