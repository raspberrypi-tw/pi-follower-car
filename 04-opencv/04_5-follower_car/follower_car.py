#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# follower_car.py
# Find the color and move to the target (this example is for green color)
#
# Author : sosorry
# Date   : 09/03/2016
# Usage  : python follower_car.py

import cv2
import pwm_motor as motor
#import dc_motor as motor

Color_Lower = (36, 130,46)
Color_Upper = (113, 255, 255)
Frame_Width  = 640
Frame_Height = 480

camera = cv2.VideoCapture(0)
camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,  Frame_Width)
camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, Frame_Height)

try:
    while True:
        (_, frame) = camera.read()

        # Do gaussian blur if needed
        frame = cv2.GaussianBlur(frame, (11, 11), 0)

        # Convert to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Convert to binary with given color
        mask = cv2.inRange(hsv, Color_Lower, Color_Upper)

        # Do erode if needed
        #mask = cv2.erode(mask, None, iterations=2)

        # Do dilate if needed
        #mask = cv2.dilate(mask, None, iterations=2)

        # Find the contours
        (contours, _) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #(contours, _) = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Define mass center
        center = None


        if len(contours) > 0:

            # Find the max length of contours
            c = max(contours, key=cv2.contourArea)

            # Find the x, y, radius of given contours        
            ((x, y), radius) = cv2.minEnclosingCircle(c)

            # Find the moments
            M = cv2.moments(c)


            try:
                # mass center
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                if radius > 10:
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)


                    # Forward and backward rule
                    if radius < 90:
                        motor.forward()

                    elif radius > 100:
                        motor.backward()

                    else:
                       motor.stop()


                    # Turn right and turn left rule
                    if center[0] > Frame_Width/2 + 10:
                        motor.turnRight()

                    elif center[0] < Frame_Width/2 - 10:
                        motor.turnLeft()

                    else:
                       motor.stop()

            except:
                pass


        # mark these lines below if you don't need to display and the car will get faster
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        # mark these lines above if you don't need to display and the car will get faster

finally:
        motor.cleanup()
        camera.release()
        cv2.destroyAllWindows()


