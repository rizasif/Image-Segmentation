import cv2
import numpy as np
import math
from pyclustering.cluster.xmeans import xmeans
from pyclustering.utils import draw_clusters
from pyclustering.cluster.xmeans import splitting_type

MIN_DIAGONAL_LENGTH = 16

def getMinMax(alist):
	z = zip(*alist)
	a = map(min, z)
	b = map(max, z)
	return [tuple(a), tuple(b)]

def checkValidBound(bound):
	diagonal = math.sqrt( math.pow(bound[0][0]-bound[1][0], 2) + math.pow(bound[0][1]-bound[1][1], 2) )
	if(diagonal < MIN_DIAGONAL_LENGTH):
		return False
	else:
		return True

def showImage(name, img):
	cv2.imshow(name, img)
	cv2.waitKey(1)

def closeWindows():
	cv2.destroyAllWindows()

def SegmentImage(image_name):
	img = cv2.imread(image_name)
	gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	sift = cv2.xfeatures2d.SIFT_create()
	kp = sift.detect(gray,None) #keypoints

	kpArray = []
	for k in kp:
		kpArray.append(k.pt)

	h, w, channels = img.shape 

	start_centers = [(w/2, h/2), (w,0), (w,h/2), (w/2,h), (0,h), (0,0), (h/2,0), (0,w/2)]

	xmeans_instance = xmeans(data=kpArray, kmax=20, initial_centers=start_centers, tolerance= 0.000001,
			criterion=splitting_type.BAYESIAN_INFORMATION_CRITERION)
	xmeans_instance.process()
	clusters = xmeans_instance.get_clusters()

	clusterList = []
	clusterBound = []
	for i in range(len(clusters)):
		clusterList.append([])
		cluster_index = len(clusterList)-1
		for c in clusters[i]:
			clusterList[cluster_index].append(( int(round(kpArray[c][0])), int(round(kpArray[c][1])) ))
		bound = getMinMax(clusterList[cluster_index])

		isBoundValid = checkValidBound(bound)

		if(isBoundValid):
			clusterBound.append(bound)
			img = cv2.rectangle(img.copy(), clusterBound[cluster_index][0], clusterBound[cluster_index][1], (0,0,255))
			center = ( (clusterBound[cluster_index][0][0]+clusterBound[cluster_index][1][0])/2,
						(clusterBound[cluster_index][0][1]+clusterBound[cluster_index][1][1])/2 )
			img = cv2.putText(img.copy(), str(cluster_index), center, cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
		else:
			clusterList.pop(cluster_index)
	return img, clusterList, clusterBound

# a,b,c = SegmentImage("Asset2.jpg")
# cv2.imshow("output",a)
# cv2.waitKey(0)