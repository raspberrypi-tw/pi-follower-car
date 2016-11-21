#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# gaussian_blur.py
# Do the Gaussian Blur effect for loaded image or image from camera
#
# Author : sosorry
# Date   : 08/31/2016
# Usage  : python gaussian_blur.py lena512rgb.png
# Usage  : python gaussian_blur.py

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


cv2.imshow("Normal", image)
cv2.waitKey(0)

blur = cv2.GaussianBlur(image, (9,9), 0)
cv2.imshow("GaussianBlur", blur)
cv2.waitKey(0)

try:
    cap.release()
except NameError:
    pass
finally:
    cv2.destroyAllWindows()


