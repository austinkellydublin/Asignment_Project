### route
from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from aircraft import *
from itertools import *



class Route:
    def __init__(self,home,port1,port2,port3,port4,port5='XXX'):
        self.port1 = Airport(home)
        self.port2 = Airport(port1)
        self.port3 = Airport(port2)
        self.port4= Airport(port3)
        self.port5 = Airport(port4)
        if port5 != 'XXX':
            self.port6 = Airport(port5)
            self.port7 = Airport(home)
        else:
            self.port6 = Airport(home)
            self.port7 = Airport(home)
        self.calclegs()
        self.portlist=[self.port1,self.port2,self.port3,self.port4,self.port5,self.port6,self.port7]


        candidates={}
        route5 = list(permutations([port2,port3,port4,port5]))
        route6a = list(permutations([port2,port2, port3, port4, port5]))
        route6b = list(permutations([port2,port3 ,port3, port4, port5]))
        route6c = list(permutations([port2, port3, port4,port4, port5]))
        route6d = list(permutations([port2, port3, port4,port5, port5]))
        #print(len(route6b))
       # print(len(route6a)) check number of permutations

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
        self.candidates=candidates
       # print(self.candidates)
       # print(len(self.candidates))
        self.portsinrange()


    def calclegs(self):
        self.leg1 =  Calcdistance(self.port1.longitude, self.port1.latitude,self.port2.longitude,self.port2.latitude).distance
        self.leg2 =  Calcdistance(self.port2.longitude,self.port2.latitude,self.port3.longitude,self.port3.latitude).distance
        self.leg3 =  Calcdistance(self.port3.longitude,self.port3.latitude,self.port4.longitude,self.port4.latitude).distance
        self.leg4 =  Calcdistance(self.port4.longitude,self.port4.latitude,self.port5.longitude,self.port5.latitude).distance
        self.leg5 =  Calcdistance(self.port5.longitude,self.port5.latitude,self.port6.longitude,self.port6.latitude).distance
        self.leg6 =  Calcdistance(self.port6.longitude,self.port6.latitude,self.port7.longitude,self.port7.latitude).distance
        self.legslist = [self.leg1, self.leg2, self.leg3 ,self.leg4, self.leg5, self.leg6]

        self.routedist = (self.leg1 +  self.leg2 + self.leg3 + self.leg4 + self.leg5 + self.leg6 )

        print('leg1', self.leg1,'  leg2', self.leg2,'  leg3', self.leg3,'  leg4', self.leg4,'  leg5', self.leg5,'  leg6', self.leg6)
        #print(self.routedist)
# craft= Aircraft('777')
# print('range  :',craft.range)
    def portsinrange(self):
        ranger= 5000

        self.portlist_inrange = {}
        #rangedict={}
        for i in range(0,6):
            #print(i)
            self.portlist_inrange[i]=[]
            rangelist = []
            strikerange = 0
            for k in range(i,6): # only consider legs beyond airport to build dictionary of lists for reach port from a given airport
                if (strikerange + self.legslist[k]) < ranger: #if haven't gone beyond range examine next leg as candidate for reachables
                    strikerange += self.legslist[k] #increment distance would have travelled
                    rangelist.append(self.portlist[k+1].code) # append end port to reachable list
                    self.portlist_inrange[i] = rangelist # update list of reachable ports for a given airport
                    #print(self.portlist_inrange)
                else: break
        print(self.portlist_inrange)
        #print([self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code])
        #print(self.portlist[3].code)

x = Route('DUB', 'LHR', 'YYJ', 'YYH', 'YYN', 'DUB')








        # dist2home = self.routedist
        # for index, airport in enumerate(self.portlist): ##go through airport and build a set of reachable ports
        #
        #     legreach=0
        #     portsinrange={}
        #     RANGE=craft.range ###########################################################TODO##############
        #     for i in range(index:6):
        #     totallegdist=leg
















