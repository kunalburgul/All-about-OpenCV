# Importing the Libraries
import cv2

# Reading the Image from the file using imread()
img = cv2.imread('data/lena.jpg', -1) # Can be (0 = Grayscale mode ,1 = Color Mode, -1 = image as it is including the aplha channel )
cv2.imshow('Leans Image',img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    # Writing the image to the file using imwrite()
    cv2.imwrite('Output/lena_copy.png', img)

