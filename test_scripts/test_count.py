import cv2
import numpy as np

img = cv2.imread('Asset.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow("Thresh", thresh)

# find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)[-2]

cnts = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print len(cnts)