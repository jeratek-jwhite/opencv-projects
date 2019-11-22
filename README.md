# opencv-projects
openCV modules and libraries

# camera_ball_tracking
This code is based entirely on the work of Adrian Rosebrock with 
minor modifications for my own use as a module. Please visit Adrian's
pyimagesearch.com site and follow him, sign up for a course, or buy a 
book. His contributions to learning opencv and machine learning are 
vast and worth your time if you are interested in learning the subject.
This specific code is based on the following code of his:
https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

Usage:
~~~
myObj = ballTrack([HSV low end array values], [HSV high end array values], [minimum radius], [camera source], [window frame width])
~~~

Example:
~~~
myObj = ballTrack((0,0,0), (255,255,255), 10, 0, 600)
myObj.StartCam()
while True:
    myImageFrame = myObj.detect()
    myBallPosition = (myObj.ballX, myObj.ballY)
    myBallRadius = myObj.ballRadius
    cv2.imshow("My Window", myImageFrame)
~~~

# camera_range_detector
This code is based entirely on the work of Adrian Rosebrock with 
minor modifications for my own use as a module. Please visit Adrian's
pyimagesearch.com site and follow him, sign up for a course, or buy a 
book. His contributions to learning opencv and machine learning are 
vast and worth your time if you are interested in learning the subject.
This specific code is based on the following code of his:
https://github.com/jrosebr1/imutils/blob/master/bin/range-detector


USAGE: 
~~~
camRangeDetector([camera name], [camera source], [min HSV array values], [max HSV array values])
rangeDetect()
~~~
Example:
~~~
myDetector = camRangeDetector("My Camera", 1, (0, 0, 0), (255, 255, 255))
myDetector.rangeDetect()
hsvLower = myDetector.hsvLower
hsvUpper = myDetector.hsvUpper
~~~
