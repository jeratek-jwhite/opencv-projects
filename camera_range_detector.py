# This code is based entirely on the work of Adrian Rosebrock with 
# minor modifications for my own use as a module. Please visit Adrian's
# pyimagesearch.com site and follow him, sign up for a course, or buy a 
# book. His contributions to learning opencv and machine learning are 
# vast and worth your time if you are interested in learning the subject.
# This specific code is based on the following code of his:
#
# https://github.com/jrosebr1/imutils/blob/master/bin/range-detector
# 
# 
#
# USAGE: 
# camRangeDetector([camera name], [camera source], [min HSV array values], [max HSV array values])
# rangeDetect()
# 
# example:
# myDetector = camRangeDetector("My Camera", 1, (0, 0, 0), (255, 255, 255))
# myDetector.rangeDetect()
# hsvLower = myDetector.hsvLower
# hsvUpper = myDetector.hsvUpper


import cv2

class camRangeDetector():
    def __init__(self, cameraName = "Camera", cameraSource=0, hsvLower = (0, 0, 0), hsvUpper = (255, 255, 255)):
        self.cameraName = cameraName
        self.cameraSource = cameraSource
        self.hsvLower = hsvLower
        self.hsvUpper = hsvUpper
        
    def callback(self, value):
        pass


    def setup_trackbars(self):
        cv2.namedWindow(self.cameraName + " Trackbars", 0)

        for i in ["MIN", "MAX"]:
            v = 0 if i == "MIN" else 255

            for j in 'HSV':
                cv2.createTrackbar("%s_%s" % (j, i), self.cameraName +" Trackbars", v, 255, self.callback)


    def get_trackbar_values(self):
        values = []

        for i in ["MIN", "MAX"]:
            for j in 'HSV':
                v = cv2.getTrackbarPos("%s_%s" % (j, i), self.cameraName + " Trackbars")
                values.append(v)

        return values


    def rangeDetect(self):
        
        camera = cv2.VideoCapture(self.cameraSource)

        self.setup_trackbars()

        while True:
            ret, image = camera.read()

            if not ret:
                break

            frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = self.get_trackbar_values()

            thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

            cv2.imshow(self.cameraName + " Original", image)
        
            cv2.imshow(self.cameraName + " Thresh", thresh)

            self.hsvLower = (v1_min, v2_min, v3_min)

            self.hsvUpper = (v1_max, v2_max, v3_max)

            # wait for key press to take action
            key = cv2.waitKey(1) & 0xFF
        
            if key == ord("q"):
                cv2.destroyAllWindows()
                break

