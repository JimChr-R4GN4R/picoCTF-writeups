# Python3 program for reverse geocoding. 

# importing necessary libraries 
import json
from subprocess import call

try:
    import reverse_geocoder as rg 
except:
    print("I will install reverse_geocoder module...")
    print("################################# INSTALLING #################################")
    install_reverse_geocoder = call("pip3 install reverse_geocoder", shell=True)
    print("################################# INSTALLED #################################")






# Put here your cords.
cords = '(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)'


##################################### If you want,you can add any special characters here to delete like '/' etc.
cords = cords.replace('_' , '')  ##
###################################

#############################################################################################
cords = cords.replace(')(' , ' ').replace('(' , '').replace(')' , '').replace(', ' , '_')  #### Make the format
cords= cords.split(' ')                                                                    ##
#############################################################################################


num_of_cords = len(cords) # 




for i in range(0, num_of_cords): # repeat until all coordinates are covered.

    print('====================================================')
    now_pos = str(cords[i])
    now_pos = now_pos.split('_') 
    cord1 = float(now_pos[0])
    cord2 = float(now_pos[1])

    def reverseGeocode(coordinates):

        result = rg.search(coordinates) 
        
        #########################################
        result_json = json.dumps(result)       #### Convert results to JSON format
        result_json = json.loads(result_json)  ##
        #########################################


        ############################################################################
                                                                                 ####### Print results
        print("Lat:",result_json[0]['lat'])###                                   ###
                                            #### Print current cords
        print("Lon:",result_json[0]['lon'])###
        
        ###################################################
        if result_json[0]['name'] == "":                 ##
            print("Name: <None>")                        ##
        else:                                            ##
            print("Name:",result_json[0]['name'])        ##
        ###################################################


        ###################################################
        if result_json[0]['admin1'] == "":               ##
            print("Admin1: <None>")                      ##
        else:                                            ##
            print("Admin1:",result_json[0]['admin1'])    ##
        ###################################################

        ###################################################
        if result_json[0]['admin2'] == "":               ##
            print("Admin2: <None>")                      ##
        else:                                            ##
            print("Admin2:",result_json[0]['admin2'])    ##
        ###################################################

        ###################################################
        if result_json[0]['cc'] == "":                   ##
            print("CC: <None>")                          ##
        else:                                            ##
            print("CC:",result_json[0]['cc'])            ##                              
        ###################################################

                                                                                 ###
                                                                                 ###
        ############################################################################

        print (Final_text)
    # Driver function 
    if __name__=="__main__": 
        
        # Coorinates tuple.Can contain more than one pair. 
        coordinates =(cord1, cord2) 
        
        reverseGeocode(coordinates) 

    print ('====================================================\n\n')


############## Useful sources for the script ##############
#https://www.geeksforgeeks.org/python-reverse-geocoding-to-get-location-on-a-map-using-geographic-coordinates/
