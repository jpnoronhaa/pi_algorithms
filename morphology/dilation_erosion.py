import cv2
import numpy as np
  
img = cv2.imread('plate.jpg', 0)

kernel = np.ones((3, 3), np.uint8)

img_dilation = cv2.dilate(img, kernel, iterations=1)
img_erosion = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('bin-plate.jpg', img)
cv2.imwrite('dilated-plate.jpg', img_dilation)
cv2.imwrite('eroded-plate.jpg', img_erosion)