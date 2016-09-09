#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# color_space.py
# Change color space from RGB to Gray, HSV. Show the effect of threshold, bitwisw operation.
#
# Author : sosorry
# Date   : 08/30/2016
# Usage  : python color_space.py ../lena512rgb.png
# Usage  : python color_space.py

import cv2
import sys
import numpy as np

# image from file
try:
    imagePath = sys.argv[1]
    image = cv2.imread(imagePath)

# image from camera
except:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  640)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    # get the 3rd photo because the first two photos are noisy
    (_, image) = cap.read()
    (_, image) = cap.read()
    (_, image) = cap.read()


cv2.imshow("Normal", image)

# Convert BGR to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Threshold the gray image to binary image
(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary", binary)

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# Define range of purple color in HSV
lower = np.array([141, 0, 0])
upper = np.array([164, 145, 197])

# Threshold the HSV image to get only purple colors
mask = cv2.inRange(hsv, lower, upper)
cv2.imshow("Mask", mask)

# Bitwise-AND mask and original image
bitwise = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Bitwise", bitwise)

cv2.waitKey(0)

try:
    cap.release()
except NameError:
    pass
finally:
    cv2.destroyAllWindows()

