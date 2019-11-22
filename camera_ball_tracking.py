# This code is based entirely on the work of Adrian Rosebrock with 
# minor modifications for my own use as a module. Please visit Adrian's
# pyimagesearch.com site and follow him, sign up for a course, or buy a 
# book. His contributions to learning opencv and machine learning are 
# vast and worth your time if you are interested in learning the subject.
# This specific code is based on the following code of his:
#
# https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
# 
# 
# Usage:
# myObj = ballTrack([HSV low end array values], [HSV high end array values], [minimum radius], [camera source], [window frame width])
# 
# Example:
# myObj = ballTrack((0,0,0), (255,255,255), 10, 0, 600)
# myObj.StartCam()
# while True:
#     myImageFrame = myObj.detect()
#     myBallPosition = (myObj.ballX, myObj.ballY)
#     myBallRadius = myObj.ballRadius
#     cv2.imshow("My Window", myImageFrame)
#
#

# import the necessary packages
import collections
from imutils.video import VideoStream
import numpy as np
import cv2
import imutils
import time

# Define ballTrack class
class ballTrack():
    def __init__(self, hsvLower = (0, 0, 0), hsvUpper = (180, 255, 255), minRadius = 10, cameraSrc = 0, maxFrameWidth = 600):
        self.hsvLower = hsvLower
        self.hsvUpper = hsvUpper
        self.cameraSrc = cameraSrc
        self.ballX = 0
        self.ballY = 0
        self.ballRadius = 0
        self.vs = None
        self.minRadius = minRadius
        self.maxFrameWidth = maxFrameWidth

    def startCam(self):    
        # if a video path was not supplied, grab the reference
        # to the webcam
        self.vs = VideoStream(src=self.cameraSrc).start()

        # allow the camera or video file to warm up
        time.sleep(2.0)

    def detect(self):
        self.ballX = 0
        self.ballY = 0
        self.ballRadius = 0

        # grab the current frame
        frame = self.vs.read()
        #args=vars
        #frame = frame[1] if 1==1 else frame
        #if isinstance(frame, collections.Sequence):
        if True:
        
            # resize the frame, blur it, and convert it to the HSV
            # color space
            frame = imutils.resize(frame, width=600)
            blurred = cv2.GaussianBlur(frame, (11, 11), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
            # construct a mask for the selected HSV values, then perform
            # a series of dilations and erosions to remove any small
            # blobs left in the mask
            mask = cv2.inRange(hsv, self.hsvLower, self.hsvUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
        
            # find contours in the mask and initialize the current
            # (x, y) center of the ball
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            center = None
        
            # only proceed if at least one contour was found
            if len(cnts) > 0:
                # find the largest contour in the mask, then use
                # it to compute the minimum enclosing circle and
                # centroid
                c = max(cnts, key=cv2.contourArea)
                ((self.ballX, self.ballY), self.ballRadius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            
                # only proceed if the radius meets a minimum size
                if self.ballRadius > self.minRadius:
                    # draw the circle and centroid on the frame,
                    # then update the list of tracked points
                    cv2.circle(frame, (int(self.ballX), int(self.ballY)), int(self.ballRadius), (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
                    return frame
                else:
                    ballX = None
                    ballY = None
                    ballRadius = None
                    return frame
            else:
                ballX = None
                ballY = None
                ballRadius = None
                return frame
        else:
            ballX = None
            ballY = None
            ballRadius = None
            return frame