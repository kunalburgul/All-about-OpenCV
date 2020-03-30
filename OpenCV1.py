import cv2

img = cv2.imread('Data/samples/data/lena.jpg', ) # Can be (0 = Grayscale mode ,1 = Color Mode, -1 = image as it is including the aplha channel )

print(img)