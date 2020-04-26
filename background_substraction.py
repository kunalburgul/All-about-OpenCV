import cv2 

cap = cv2.VideoCapture('data/vtest.avi')
fgbg = cv2.bgsegm.createBackgroundSubstractorMOG()
#fgbg = cv2.bgsegm.createBackgroundSubstractorMOG2(detectShadows=False)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
#fgbg = cv2.bgsegm.createBackgroundSubstractorGMG()
#fgbg = cv2.bgsegm.createBackgroundSubstractorKNN(detectShadows=False)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)

    keyboard = cv2.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()