##calculate leg distances

from __airport import  *
from calculatedistance import *



class Legdistances():
    def __init__(self, port1, port2, port3, port4, port5,port6,port7='!!!'):
        self.port1 = Airport(port1)
        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4 = Airport(port4)
        self.port5 = Airport(port5)
        self.port6 = Airport(port6)  ## need to reasign these for permutations

        if port7=='!!!':
            self.port7=self.port6
        else:
            self.port7 = Airport(port7)

        self.calclegs()



    def calclegs(self):
                self.leg1 = int \
                    (Calcdistance(self.port1.longitude, self.port1.latitude, self.port2.longitude,
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
                self.legslist = [self.leg1, self.leg2, self.leg3, self.leg4, self.leg5, self.leg6]

                self.routedist = (self.leg1 + self.leg2 + self.leg3 + self.leg4 + self.leg5 + self.leg6)
               # print(self.legslist)
               # print(self.routedist)

x = Legdistances('SXR', 'TNI', 'AGX', 'BLR', 'YYU','SXR','TNI')
