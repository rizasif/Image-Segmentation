import os
import sys
import ImageSegmentation as IS
from DataBank import DataBank

class DataEntry():

	class STATUS():
		ERROR = 500
		DONE = 200
		RESET = 300
		EXIT = 100
		ALL = 800
		NONE = 600

	def __init__(self):
		self.folder_name = "testSetPlaces205_resize/testSet_resize"
		self.imgList = list(os.listdir(self.folder_name))
		self.imgList.sort()

		self.DB = DataBank()

		bookmark = self.DB.get_last_row_as_list()

		if not bookmark is None:
			self.list_start = self.imgList.index(bookmark[0]) + 1
		else:
			self.list_start = 0
	
	def is_number(self, s):
		try:
			int(s)
			return True
		except ValueError:
			return False

	def handleInput(self, iput, inputData, num_clusters):
		status = self.STATUS.NONE

		# d = done, r = reset, e = exit
		if(not self.is_number(iput)):
			if(iput == 'r'):
				status = self.STATUS.RESET
			elif(iput == 'd'):
				status = self.STATUS.DONE
			elif(iput == 'a'):
				status = self.STATUS.ALL
			elif(iput == 'e'):
				status = self.STATUS.EXIT
			else:
				status = self.STATUS.ERROR
				print "Invalid Input, try again"
		elif(int(iput) >= num_clusters):
			status = self.STATUS.ERROR
			print "Cluster number does not exist, try again"
		else:
			inputData.append(int(iput))
			
		return status, inputData


	def begin(self):
		if(self.list_start > len(self.imgList)-1):
			print "All images in folder processed"
			sys.exit()

		for i in range(self.list_start, len(self.imgList)):
			image_name = self.imgList[i]

			img, clusterList, clusterBound = IS.SegmentImage(self.folder_name + "/" + image_name)
			IS.showImage(image_name, img)

			print "-----------------\nImage: " + image_name + "\nAvailable Inputs [d = Done, a=Select All, r = Reset, e = Exit]"
			blur_clusters = []
			while True:
				print "Clusters Selected: ", blur_clusters
				input_data = raw_input("Input: ")
				status, blur_clusters = self.handleInput(input_data, blur_clusters, len(clusterList))
				
				if(status == self.STATUS.NONE):
					continue
				elif(status == self.STATUS.DONE):
					self.DB.insert_data(name=image_name,
										num_of_clusters=len(clusterList),
										cluster_contours=clusterBound,
										blur_clusters=blur_clusters,
										valid_image = (len(clusterList)>=len(blur_clusters)) )
					break
				elif(status == self.STATUS.ALL):
					self.DB.insert_data(name=image_name,
										num_of_clusters=len(clusterList),
										cluster_contours=clusterBound,
										blur_clusters=[-1],
										valid_image = False )
					break
				elif(status == self.STATUS.RESET):
					blur_clusters = []
					IS.closeWindows()
					IS.showImage(image_name, img)
				elif(status == self.STATUS.ERROR):
					pass
				elif(status == self.STATUS.EXIT):
					IS.closeWindows()
					sys.exit()

			IS.closeWindows()
			print "Your Choice is: ", blur_clusters

DE = DataEntry()
DE.begin()