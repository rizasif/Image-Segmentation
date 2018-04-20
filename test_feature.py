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
# clusters = xmeans_instance.get_centers()

# for c in clusters:
# 	img = cv2.circle(img.copy(), ( int(round(c[0])), int(round(c[1])) ), 5, (255,0,0), -1)

for c in clusters[0]:
	img = cv2.circle(img.copy(), ( int(round(kpArray[c][0])), int(round(kpArray[c][1])) ), 5, (255,0,0), -1)

cv2.imshow("output", img)

# print clusters

# print xmeans_instance.get_cluster_encoding()

# draw_clusters(data=kpArray, clusters=clusters, marker_descr="+")
cv2.waitKey(0)

#data=[(1,1),(2,2), (5,5),(4,4),(8,8),(7,7)]
