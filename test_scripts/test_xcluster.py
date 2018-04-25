from pyclustering.cluster.xmeans import xmeans
from pyclustering.utils import draw_clusters
from pyclustering.cluster.xmeans import splitting_type

kpArray = [   (1,1),   (2,2),   (3,3),
 			(15,15), (14,14), (16,16),
			(28,28), (27,27), (29,29),
			(70,70) ]

xmeans_instance = xmeans(data=kpArray, kmax=10, initial_centers=[(0,0), (20,20), (30,30), (40,40), (50,50)],
	 criterion=splitting_type.MINIMUM_NOISELESS_DESCRIPTION_LENGTH)
xmeans_instance.process()
# clusters = xmeans_instance.get_clusters()
clusters = xmeans_instance.get_centers()

print clusters

# draw_clusters(data=kpArray, clusters=clusters, marker_descr="+")

#data=[(1,1),(2,2), (5,5),(4,4),(8,8),(7,7)]
