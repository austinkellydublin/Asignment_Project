### route
from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from aircraft import *
from itertools import *

class Route:
    def __init__(self,home,port1,port2,port3,port4,port5='XXX'):
        self.home  = Airport(home)
        self.port1 = Airport(port1)
        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4 = Airport(port4)
        if port5 != 'XXX':
            self.port5 = Airport(port5)
            self.port6 = Airport(home)
        else:
            self.port5 = Airport(home)
            self.port6 = Airport(home)
        self.calclegs()

        candidates={}
        route5 = list(permutations([port1,port2,port3,port4]))
        route6a = list(permutations([port1,port1, port2, port3, port4]))
        route6b = list(permutations([port1,port2 ,port2, port3, port4]))
        route6c = list(permutations([port1, port2, port3,port3, port4]))
        route6d = list(permutations([port1, port2, port3,port4, port4]))
        print(len(route6b))
        print(len(route6a))

        for index, eachlist in (enumerate(route5)):
            candidates[index] =[home] + list(eachlist) + [home]
        for index, eachlist in (enumerate(route6a)):
            candidates[24+index] = [home] + list(eachlist) + [home]
        for index, eachlist in (enumerate(route6b)):
            candidates[144 + index] = [home] + list(eachlist) + [home]
        for index, eachlist in (enumerate(route6c)):
            candidates[264 + index] = [home] + list(eachlist) + [home]
        for index, eachlist in (enumerate(route6d)):
            candidates[384 + index] = [home] + list(eachlist) + [home]





       # self.candidatesroutes = candidates
        print(candidates)
        print(len(candidates))








       # print(candidateroutes)
        # for i in







    def calclegs(self):
        self.leg1 =  Calcdistance(self.home.longitude, self.home.latitude,self.port1.longitude,self.port1.latitude).distance
        self.leg2 =  Calcdistance(self.port1.longitude,self.port1.latitude,self.port2.longitude,self.port2.latitude).distance
        self.leg3 =  Calcdistance(self.port2.longitude,self.port2.latitude,self.port3.longitude,self.port3.latitude).distance
        self.leg4 =  Calcdistance(self.port3.longitude,self.port3.latitude,self.port4.longitude,self.port4.latitude).distance
        self.leg5 =  Calcdistance(self.port4.longitude,self.port4.latitude,self.port5.longitude,self.port5.latitude).distance
        self.leg6 =  Calcdistance(self.port5.longitude,self.port5.latitude,self.port6.longitude,self.port6.latitude).distance

        self.routedist = (self.leg1 +  self.leg2 + self.leg3 + self.leg4 + self.leg5 + self.leg6 )


       # print('leg1  ', self.leg1,'leg2  ', self.leg2,'leg3  ', self.leg3,'leg4  ', self.leg4,'leg5  ', self.leg5,'leg6  ', self.leg6)
       # print(self.routedist)





x= Route('DUB','LHR','YYJ','YYH','YYN','DUB')








