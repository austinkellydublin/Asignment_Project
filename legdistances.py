##calculate leg distances
#version 1.0
###Author Austin Kelly
'''this module calculates the legs distances for a route it takes the route as seperate string parameters and stores key distance information in its attributes'''


from __airport import  *
from calculatedistance import *



class Legdistances():##main class to calculate distances in each stage of a journey note you return to first port
    def __init__(self, port1, port2, port3, port4, port5,port6,port7='!!!'):
        self.port1 = Airport(port1)

        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4 = Airport(port4)
        self.port5 = Airport(port5)
        self.port6 = Airport(port6)

        if port7=='!!!':##this is so can use same code base to generate five leg and six leg journeys form our permutations (last leg will be zero in five leg)
            self.port7=self.port6
        else:
            self.port7 = Airport(port7)
##call the calclegs method to generate stage distances stored in leg# fields


    ###calclegs uses the calcdistance module to calculate the distance between a set of airports and sets the distances in propertie
        self.leg1 =int(Calcdistance(self.port1.longitude, self.port1.latitude, self.port2.longitude,
                          self.port2.latitude).distance)
        self.leg2 = int \
            (Calcdistance(self.port2.longitude, self.port2.latitude, self.port3.longitude,
                          self.port3.latitude).distance)
        self.leg3 = int \
            (Calcdistance(self.port3.longitude, self.port3.latitude, self.port4.longitude,
                          self.port4.latitude).distance)
        self.leg4 = int \
            (Calcdistance(self.port4.longitude, self.port4.latitude, self.port5.longitude,
                          self.port5.latitude).distance)
        self.leg5 = int \
            (Calcdistance(self.port5.longitude, self.port5.latitude, self.port6.longitude,
                          self.port6.latitude).distance)
        self.leg6 = int \
            (Calcdistance(self.port6.longitude, self.port6.latitude, self.port7.longitude,
                          self.port7.latitude).distance)
        self.legslist = [self.leg1, self.leg2, self.leg3, self.leg4, self.leg5, self.leg6]#distances in an convenience array/list

        self.routedist = (self.leg1 + self.leg2 + self.leg3 + self.leg4 + self.leg5 + self.leg6)#total distance in route
           # print(self.legslist)
           # print(self.routedist)

def main(): # this function performs a test on the module it should return results below
    x = Legdistances('SXR', 'TNI', 'AGX', 'BLR', 'YYU','SXR','TNI')
    print('The distances of each leg are ',x.legslist)
    print('The total distance is ',x.routedist)
    x
if __name__ == '__main__':
    main()
#test results should return-------- The distances of each leg are  [1201, 1781, 642, 12812, 10472, 1201].....The total distance is  28109
