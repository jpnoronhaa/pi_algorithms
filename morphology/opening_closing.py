
import cv2
import numpy as np

img = cv2.imread("plate.jpg", 0)

bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.ones((3, 3), np.uint8)

opening = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel, iterations=1)
closing = cv2.morphologyEx(bin_img, cv2.MORPH_CLOSE, kernel, iterations=1)


cv2.imwrite('opened-plate.jpg', opening)
cv2.imwrite('closed-plate.jpg', closing)
