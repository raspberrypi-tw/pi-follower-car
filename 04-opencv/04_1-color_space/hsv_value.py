#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hsv_value.py
# Choose the HSV value in real-time
#
# Author : Aruldd
# Usage  : python choose_hsv_value.py ../lena512rgb.png
# Origin : http://stackoverflow.com/questions/10948589/choosing-correct-hsv-values-for-opencv-thresholding-with-inranges

import cv2
import numpy as np
import sys


def nothing(x):
    pass


# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('hl', 'result', 0,   179, nothing)
cv2.createTrackbar('hu', 'result', 179, 179, nothing)
cv2.createTrackbar('sl', 'result', 0,   255, nothing)
cv2.createTrackbar('su', 'result', 255, 255, nothing)
cv2.createTrackbar('vl', 'result', 0,   255, nothing)
cv2.createTrackbar('vu', 'result', 255, 255, nothing)


imagePath = sys.argv[1]

while True:
    image = cv2.imread(imagePath)

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'result')
    hu = cv2.getTrackbarPos('hu', 'result')
    sl = cv2.getTrackbarPos('sl', 'result')
    su = cv2.getTrackbarPos('su', 'result')
    vl = cv2.getTrackbarPos('vl', 'result')
    vu = cv2.getTrackbarPos('vu', 'result')

    # Converting to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("result", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cv2.destroyAllWindows()
