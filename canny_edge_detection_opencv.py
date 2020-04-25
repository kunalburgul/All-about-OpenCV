import cv2
import numpy as np 
import matplotlib.pyplot as plt 

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("CMIN", "Tracking", 0, 250, nothing)
cv2.createTrackbar("CMAX", "Tracking",250, 500,nothing)

while True:
   
    img = cv2.imread('data/messi5.jpg',0)

    c_min = cv2.getTrackbarPos("CMIN", "Tracking")
    c_max = cv2.getTrackbarPos("CMAX", "Tracking")
    

    canny = cv2.Canny(img, c_min, c_max) 

    lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 1)
    lap = np.uint8(np.absolute(lap))

    cv2.imshow("canny", canny)
    cv2.imshow("lap", lap)
    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

# 200 , 350 or 300 something

#  img = cv2.imread('Data/samples/data/lena.jpg',0)

#     c_min = cv2.getTrackbarPos("CMIN", "Tracking")
#     c_max = cv2.getTrackbarPos("CMAX", "Tracking")
    

#     canny = cv2.Canny(img, c_min, c_max)

#     lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 1)
#     lap = np.uint8(np.absolute(lap))


#  titles = ['image','lap','canny']
#     images = [img,lap,canny]

#     for i in range(3):
#         plt.subplot(1,3, i+1)
#         plt.imshow(images[i], 'gray')
#         plt.title(titles[i])
#         plt.xticks([])
#         plt.yticks([])

#     plt.show()

