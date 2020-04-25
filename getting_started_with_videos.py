import cv2
import datetime

cap = cv2.VideoCapture(0) # Capturing the video

fourcc = cv2.VideoWriter_fourcc(*'XVID') # This is the fourcc code to be passed 
# Saving the Video (Here argument is FourCC code, third argumet is FPS, fouth argument is SIZE)
out = cv2.VideoWriter('output/video_output.avi', fourcc, 20.0, (640,480) ) 



print(cap.isOpened())

while (cap.isOpened()): # To check the if the correct camera is detected or else keep it True
    ret, frame = cap.read()
     
    if ret == True:   
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Parameter to get height and width of the frame
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # OR
        print(cap.get(3))
        print(cap.get(4))


        # # We can also set to the particular value using the cap.set()
        # cap.set(CAP_PROP_FRAME_WIDTH)
        # # OR 
        # cap.set(3, 1208)
        # cap.set(4, 720 )

        
        #####################################################
        # Printing the Current Date and Time and Other text in the video
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now()) # Shows the current date and time 
        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)
 


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting to the gray scale image
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

cap.release()
out.release()
cv2.destroyAllWindows()