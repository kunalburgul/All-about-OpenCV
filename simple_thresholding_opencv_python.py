import cv2 
import numpy as np  

img = cv2.imread('data/gradient.png', 0)

# If the value of the (pixcel) < (threshold value) than that value is assigned to 0
# If the value of the (pixcel) > (threshold value) than that value is assigned to 255
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# If the value of the (pixcel) < (threshold value) than that value is assigned to 255
# If the value of the (pixcel) > (threshold value) than that value is assigned to 0
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# From 0 to the (threshold value) the value of the pixcel remains original 
# After the (threshold value) the value of the pixcel changes to (threshold value) 
# If the value of the (pixcel) < (threshold value) than value remains original
# If the value of the (pixcel) > (threshold value) than that value is assigned to (threshold value).
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# From 0 to the (threshold value) the value of the pixcel is assigned to 0
# After the (threshold value) the value of the pixcel remains original
# If the value of the (pixcel) < (threshold value) than value is assigned to 0
# If the value of the (pixcel) > (threshold value) than that value remains original
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# From 0 to the (threshold value) the value of the pixcel remains original
# After the (threshold value) the value of the pixcel is assigned to 0
# If the value of the (pixcel) < (threshold value) than value remains original
# If the value of the (pixcel) > (threshold value) than that value is assigned to 0
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


cv2.imshow('Image', img)

cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)
cv2.imshow('th4', th4)
cv2.imshow('th5', th5)


cv2.waitKey(0)
cv2.destroyAllWindows()