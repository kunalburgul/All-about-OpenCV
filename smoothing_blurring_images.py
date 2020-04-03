import cv2
import numpy as np 
import matplotlib.pyplot as plt 

# Homogeneous filter is the most simple filterm each output pixel is the mean of its kernel 
# neighbour

img = cv2.imread('Data/samples/data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Filtering using 2 Dimensional Convolutional
kernel = np.ones((5, 5), np.float32)/25 
dst = cv2.filter2D(img, -1, kernel)

"""
As in 1D signals images can be filtered with various low-pass filters(LPF) and the 
high-pass filter(HPF) etc. 
- Here LPF helps in removing the noises bluring the images,
- HPF filters helps in finding edges in the images
"""
blur = cv2.blur(img, (5, 5))

# Gaussian filter is nothing but using different-weight-kernel, in both x and y direction
gblur = cv2.GaussianBlur(img, (5, 5), 0)

"""
Median filter is something that replace each pixels value with the median of its neighboring picels. 
This method is great when dealing with "salt and pepper noise".
"""
# Here kernel size must be always odd except 1 
median = cv2.medianBlur(img, 5)

bilaternalFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image','2D Convolution','blur', 'gblur','median','bilateralFilter']
images = [img,dst,blur,gblur,median, bilaternalFilter]

for i in range(6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
    
plt.show()