import cv2
import numpy as np 

img = cv2.imread('data/lena.jpg')

"""
Pyramid or pyramid representation is a type of multi-scale signal representation in which a 
signal or an image is subject to repeated smoothing and subsampling.
 
There are two types of pyramid in OpenCV
1) Gaussian Pyramid
  - pyrdown
  - pyrup 
2) Laplacian pyramid

"""
'''
# Decrease the resolution of the image 
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

# Increase the resolution of the image 
hr = cv2.pyrUp(lr2)
'''
layer = img.copy()
# Gaussian pyramid array
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow("Gaussian "+str(i),layer)
"""
A level in laplacian Pyramid is formed by the difference between that level in Gassuian Pyramid and
expandeed version of its upper level in Gaussian Pyramid.
"""

layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid', layer)

lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow("laplasian "+str(i),laplacian)


cv2.imshow('Original Image', img)
# cv2.imshow('pyrDown 1 Image',lr1)
# cv2.imshow('pyrDown 2 Image',lr2)

# cv2.imshow('pyrUp Image',hr)

cv2.waitKey(0)
cv2.destroyAllWindows()

