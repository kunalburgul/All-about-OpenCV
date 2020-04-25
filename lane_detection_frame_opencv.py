import cv2
import numpy as np 
import matplotlib.pyplot as plt


img = cv2.imread('data/road_1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ROI function
def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    # channel_count = image.shape[2]
    match_mask_color = 255 # * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def draw_the_lines(image, lines):
    image = np.copy(image)
    blank_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)

    image = cv2.addWeighted(image, 0.8, blank_image, 1, 0.0)
    return image

print(img.shape)
height = img.shape[0]
width = img.shape[1]

# Region of Intrest allocating the vertices i.e lanes
region_of_interest_vertices = [
    (0, height),   # left side lane 
    (width/2, height/2), # Front deadend 
    (width, height) # right side lane
]



gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)

# ROI 
cropped_image = region_of_interest(canny_image,
                np.array([region_of_interest_vertices], np.int32),)

# Lines vector of all the lines which are detected in the ROI
lines = cv2.HoughLinesP(cropped_image, 
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

image_with_lines = draw_the_lines(img, lines)

plt.imshow(image_with_lines)
plt.show()

  