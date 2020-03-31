import numpy as np  
import cv2

# Reading the image
img = cv2.imread('Data/samples/data/lena.jpg',1)

# Creating the image using Numpy Zeros Method (This gives the black backgroung image)
img = np.zeros([512, 512, 3], np.uint8)

# Drawinf the line (img, plt, plt, BGR(BLUE, GREEN, RED), THICKNESS)
img = cv2.line(img, (0,0), (255, 255), (255, 0, 255), 6)
img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 0, 0), 6)

# Drawing the Rectangle
img = cv2.rectangle(img, (380,0 ), (510, 128), (255, 0, 255), 8) # When thickness is -1 we get the filled rectangle

# Drawing the Circle 
img = cv2.circle(img, (255,255), 63, (0, 255, 0), -1)

# Putting the text into the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpevCV', (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)



cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()