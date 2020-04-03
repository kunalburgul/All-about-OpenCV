import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread("Data/samples/data/messi5.jpg", cv2.IMREAD_GRAYSCALE) # sudoku.png
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 1)
lap = np.uint8(np.absolute(lap))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

"""
The Vanny edge detector is an edge detection operator that uses a multi-stage algorithm to 
detect a wide range of edges in images. It was developed by John F. canny in 1986 
The Canny edge detection algorithm is composed of 5 steps:
1) Noise reduction - gaussian filter
2) Gradient calculation
3) Non-maximum suppression
4) Double threshold
5) Edge Tracking by Hystersis
"""
canny = cv2.Canny(img, 100, 200 )

titles = ['image','lap','sobelX','sobelY','sobelCombined','canny']
images = [img,lap,sobelX,sobelY,sobelCombined,canny]

for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()