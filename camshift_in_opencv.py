# Object Tracking = canshift = meanshift + dynamic size 
import cv2
import numpy as np 

cap = cv2.VideoCapture('data/traffic.mp4')
# Take First frame of the Video
ret, frame = cap.read()
# Setup initial location of window
x, y, width, height = 300, 200, 100, 50
track_window = (x, y, width, height)

# Setup the ROI for Tracking
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255)))
roi_hist = cv2.calcHist(hsv_roi, [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
cv2.imshow('roi',roi)

while(1):
    ret, frame = cap.read()
    if ret == True:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180],1)
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        pts = cv2.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        final_image = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv2.imshow('dst', dst)
        cv2.imshow('frame', frame)
        # cv2.imshow('roi',roi)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break