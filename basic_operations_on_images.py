import numpy as np 
import cv2

img = cv2.imread('Data/samples/data/messi5.jpg',1)

print(img.shape) # Return a tuple of number of rows, columns and channels
print(img.size) # Returns Total number of pixcels is accessed
print(img.dtype) # Returns Image datatype is obatined 
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# Copy the image from one position to the other
ball = img[280:340, 330:390] # Copied the ball
img[273:333, 100:160] = ball # Placing the ball on the new coordinates

# Add the new Image to the existing Image
# In order to add two image you should have both of them of the same size
img2 = cv2.imread('Data/samples/data/opencv-logo.png')

img = cv2.resize(img, (512, 512))  # Resizing the img 
img2 = cv2.resize(img2, (512, 512)) # Resizing the img2

dst = cv2.add(img, img2)
dstwt = cv2.addWeighted(img, .9, img2, .1, 0)

cv2.imshow('image', dstwt)
cv2.waitKey(0)
cv2.destroyAllWindows()
