#calculatedistance
#version 1.0
###Author Austin Kelly
'''this module calculates the distances between two points on earth as crow flys using the formula provided by lecuturer for course D265'''

import math##need some methods from the math library

class Calcdistance:## the initialization takes the longitude and latitudes as string variable and calls its caldist method which returns the distance andn this is stored in the distance attribute
    def __init__(self,longitude1,latitude1,longitude2,latitude2):
        self.longitude = longitude1
        self.latitude = latitude1
        self.longitude2 = longitude2
        self.latitude2 = latitude2
        self.distance = self.calcdist()##this calls the calcdist method and the return is stored in the distance parameter


    def calcdist(self):# this is the main logic of the module and performs the calculation
        theta = 0.000000#initials some variable for use. for the angles
        gamma = 0.000000#
        theta2 = 0.000000#
        gamma2 = 0.000000#
        if self.latitude >= 0:##need to normalize the longitude and latitude and also convert degrees to radians for equation input
            theta = self.deg2rads(90 - self.latitude)
            # print(theta)
        else:
            theta = self.deg2rads(90 + abs(self.latitude))
            # print(theta)
        gamma = self.deg2rads(self.longitude)###
        # print('g1 ' + str(gamma))


        if self.latitude2 >= 0:
            theta2 = self.deg2rads(90 - self.latitude2)
            #  print('t2' + str(theta2))
        else:

            theta2 = self.deg2rads(90 + abs(self.latitude2))
            # print('t2b ' + str(theta2))
        gamma2 = self.deg2rads(self.longitude2)
        # print('g2 ' + str(gamma2))
        #below is the equation to calculate the distance
        dist = math.acos(math.sin(theta) * math.sin(theta2) * (math.cos(gamma - gamma2)) + (math.cos(theta)) * math.cos(
            theta2)) * 6371

        return dist #returns the distance in a variable

    def deg2rads(self, degrees):  ##function to convert degrees to rads
        rads = degrees * (2 * math.pi) / 360
        return rads


def main(): # this is a test it should return 17215.2756734028
    x=Calcdistance(-6.270075,53.421333,151.177222,-33.946111)
    print(x.distance)


if __name__=='__main__':
    main()
