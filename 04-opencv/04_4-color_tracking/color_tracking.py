#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# color_tracking.py
# Tracking color from camera in real-time
#
# Author : Aruldd
# Usage  : python color_tracking.py 
# Origin : http://stackoverflow.com/questions/10948589/choosing-correct-hsv-values-for-opencv-thresholding-with-inranges

import cv2
import numpy as np


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


cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

while True:
    (_, frame) = cap.read()

    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'result')
    hu = cv2.getTrackbarPos('hu', 'result')
    sl = cv2.getTrackbarPos('sl', 'result')
    su = cv2.getTrackbarPos('su', 'result')
    vl = cv2.getTrackbarPos('vl', 'result')
    vu = cv2.getTrackbarPos('vu', 'result')

    # Converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])
    mask = cv2.inRange(hsv, lower, upper)

    (contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)

        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            cv2.circle(frame, (int(x), int(y)), int(radius), (255, 0, 0), 5)
            cv2.circle(frame, center, 5, (255, 0, 0), -1)

        except:
            pass


    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("result", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
