import cv2 
import numpy as np 
import matplotlib.pyplot as plt

"""
- Morphological transformations are some simple operations based on the image shape.

- We will discuss different morphological processes such as Erossion, Dilation, Opening 
  and Closing methods. 

- Morphological operations can only be applied on the Binary Image

-For Morphological transformations we need two things 
1) Original Image.
2) Structuring Element or a kernel which decides the nature of the operation.

"""


img = cv2.imread('Data/samples/data/smarties.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

 # to remove the small marks in the grayscale image 
dilation = cv2.dilate(mask, kernal, iterations= 2)

# spots out the small marks in images
erosion = cv2.erode(mask, kernal, iterations = 2  ) 

# In opening first erosion is applied the dilation is applied
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal) 

# In closing first dialtion is applied anf the erosion is applied
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernal)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT,kernal)

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT,kernal)

titles = ['image','mask', 'dilation','erosion','opening','closing', 'mg', 'th']
images = [img, mask, dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
