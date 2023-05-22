import cv2
import numpy as np
  
img = cv2.imread('plate.jpg', 0)
bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

kernel = np.array([[255,255,255],[255,255,255],[255,255,255]], np.uint8)

cv2.imwrite('bin-plate.jpg', bin_img)

def dilate(img, kernel):
    dilate_img = img.copy()
    row, column = img.shape
    for i in range(1, row - 2):
        for j in range(1, column - 2):
            value = np.uint8(0)
            compare = False
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if img[i+k, j+l] == kernel[k+1,l+1]:
                        compare = True
                if compare:
                    value = np.uint8(255)
                    break
            dilate_img[i,j] = value
    return dilate_img

dilate_img = dilate(bin_img, kernel)
cv2.imwrite('dilated-plate.jpg', dilate_img)