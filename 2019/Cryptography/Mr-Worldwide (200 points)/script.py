# Python3 program for reverse geocoding. 

# importing necessary libraries 
import reverse_geocoder as rg 
import pprint 

cords = '(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)'
cords = cords.replace('_' , '')
cords = cords.replace(')(' , ' ').replace('(' , '').replace(')' , '').replace(', ' , '_')
cords= cords.split(' ')

num_of_cords = len(cords)

for i in range(0, num_of_cords):
	print('====================================================')
	now_pos = str(cords[i])
	now_pos = now_pos.split('_') 
	cord1 = float(now_pos[0])
	cord2 = float(now_pos[1])

	def reverseGeocode(coordinates): 
		result = rg.search(coordinates) 
		
		# result is a list containing ordered dictionary. 
		pprint.pprint(result) 

	# Driver function 
	if __name__=="__main__": 
		
		# Coorinates tuple.Can contain more than one pair. 
		coordinates =(cord1, cord2) 
		
		reverseGeocode(coordinates) 

	print ('====================================================\n\n')

############## Useful sources for the script ##############
#https://www.geeksforgeeks.org/python-reverse-geocoding-to-get-location-on-a-map-using-geographic-coordinates/
