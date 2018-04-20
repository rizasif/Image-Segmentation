import cv2
import numpy as np

img = cv2.imread('Asset2.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

# for k in kp:
# 	print k.pt

cv2.drawKeypoints(img, kp, img)
cv2.imwrite('sift_keypoints.jpg',img)



