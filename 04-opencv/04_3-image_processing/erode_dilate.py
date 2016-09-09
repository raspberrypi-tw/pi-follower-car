#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# erode_dilate.py
# Do the erode or dilate effect for loaded image or image from camera
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python erode_dilate.py lena512rgb.png
# Usage  : python erode_dilate.py

import cv2
import sys

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


# convert RGB to Gray to Binary
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(_, binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow("Normal", image)
#cv2.imshow("Gray", gray)
cv2.imshow("Binary", binary)

erode  = cv2.erode(binary, None, iterations=2)
cv2.imshow("Erode", erode)

#dilate = cv2.dilate(binary, None, iterations=2)
#cv2.imshow("Dilate", dilate)

cv2.waitKey(0)

try:
    cap.release()
except NameError:
    pass
finally:
    cv2.destroyAllWindows()


