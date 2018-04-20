import cv2
import numpy as np

img = cv2.imread("Asset.jpg")

# convert the mean shift image to grayscale, then apply
# Otsu's thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)