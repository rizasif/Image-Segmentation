import cv2
import numpy as np
from pyclustering.cluster.xmeans import xmeans
from pyclustering.utils import draw_clusters
from pyclustering.cluster.xmeans import splitting_type

img = cv2.imread('Asset2.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None) #keypoints

kpArray = []
for k in kp:
	kpArray.append(k.pt)

h, w, channels = img.shape 

start_centers = [(w/2, h/2), (w,0), (w,h/2), (w/2,h), (0,h), (0,0), (h/2,0), (0,w/2)]

xmeans_instance = xmeans(data=kpArray, kmax=10, initial_centers=start_centers, tolerance= 0.000001,
		criterion=splitting_type.BAYESIAN_INFORMATION_CRITERION)
xmeans_instance.process()
clusters = xmeans_instance.get_clusters()


def getMinMax(alist):
	z = zip(*alist)
	a = map(min, z)
	b = map(max, z)
	return [tuple(a), tuple(b)]

clusterList = []
clusterBound = []
for i in range(len(clusters)):
	clusterList.append([])
	for c in clusters[i]:
		clusterList[i].append(( int(round(kpArray[c][0])), int(round(kpArray[c][1])) ))
	clusterBound.append(getMinMax(clusterList[i]))

	img = cv2.rectangle(img.copy(), clusterBound[i][0], clusterBound[i][1], 3)

cv2.imshow("output", img)
cv2.waitKey(0)
