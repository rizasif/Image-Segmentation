import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("coins_01.jpg")

# # convert the mean shift image to grayscale, then apply
# # Otsu's thresholding
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 0, 255,
# 	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# # cv2.imshow("Thresh", thresh)

# # find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)[-2]
# print("[INFO] {} unique contours found".format(len(cnts)))
 
# # loop over the contours
# for (i, c) in enumerate(cnts):
# 	# draw the contour
# 	((x, y), _) = cv2.minEnclosingCircle(c)
# 	print(c)
# 	cv2.putText(img, "#{}".format(i + 1), (int(x) - 10, int(y)),
# 		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
# 	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
 
# # show the output image
# cv2.imshow("Image", img)
# cv2.waitKey(0)

# -------------------------------------------------
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
# img[markers == -1] = [255,0,0]

# cv2.imshow("Image",markers)

print len(markers)

# cv2.waitKey(0)