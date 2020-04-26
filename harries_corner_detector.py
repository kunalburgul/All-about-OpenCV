"""
# 3 Imp points to remember

1) determinw which windows produce very large variations in intensity when moved in both X and Y directions

2) With each such window found, a score R is computed.

3) After appalying a threshold to this score, important corners are selected and marked
  - 1. |R| is small, which happens when λ1 and λ2 are small, the region is flat.
  - 2. R<0, which happens when λ1>>λ2 or vice versa, the region is edge.
  - 3. R is large, which happens when λ1 and λ2 are large and λ1 ~ λ2, the region is a corner
"""

import cv2
import numpy as np 


img = cv2.imread('data/chessboard.png')

cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()