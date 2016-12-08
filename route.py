### route
from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from aircraft import *
from itertools import *



class Route:
    def __init__(self,port1,port2,port3,port4,port5,craft='777',genperms=True):  ##how coordi
        self.port1 = Airport(port1)
        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4= Airport(port4)
        self.port5 = Airport(port5)
        self.port6 = Airport(port1)## need to reasign these for permutations
        self.port7=Airport(port1)## defaults are home
        self.genperms=genperms
        self.calclegs()
        self.portlist=[self.port1,self.port2,self.port3,self.port4,self.port5,self.port6,self.port7]
        self.craft = Aircraft(craft)
        print(self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code)
        print('aircratf model :',self.craft.model)
        print('range  :',self.craft.range)
        if self.genperms==True :
            candidates={}
            route5 = list(permutations([self.port2.code,self.port3.code,self.port4.code,self.port5.code]))
            print(route5)
            route6a = list(permutations([self.port2.code,self.port2.code, self.port3.code, self.port4.code, self.port5.code]))
            print(route6a)
            route6b = list(permutations([self.port2.code,self.port3.code ,self.port3.code, self.port4.code, self.port5.code]))
            print(route6b)
            route6c = list(permutations([self.port2.code, self.port3.code, self.port4.code,self.port4.code, self.port5.code]))
            print(route6c)
            route6d = list(permutations([self.port2.code,self.port3.code, self.port4.code,self.port5.code,self.port5.code]))
            print(route6d)
            # print(len(route6a)) check number of permutations

            for index, eachlist in (enumerate(route5)):
                candidates[index] =[port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6a)):
                candidates[24+index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6b)):
                candidates[144 + index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6c)):
                candidates[264 + index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6d)):
                candidates[384 + index] = [port1] + list(eachlist) + [port1]
                self.candidates=candidates #these are airport codes codes generated from a set of routes
            print(self.candidates)
            #print(len(self.candidates))
            self.portsinrange()
        else:pass
        self.findbestroute()


    def calclegs(self):
        self.leg1 =  int(Calcdistance(self.port1.longitude, self.port1.latitude,self.port2.longitude,self.port2.latitude).distance)
        self.leg2 =  int(Calcdistance(self.port2.longitude,self.port2.latitude,self.port3.longitude,self.port3.latitude).distance)
        self.leg3 =  int(Calcdistance(self.port3.longitude,self.port3.latitude,self.port4.longitude,self.port4.latitude).distance)
        self.leg4 =  int(Calcdistance(self.port4.longitude,self.port4.latitude,self.port5.longitude,self.port5.latitude).distance)
        self.leg5 =  int(Calcdistance(self.port5.longitude,self.port5.latitude,self.port6.longitude,self.port6.latitude).distance)
        self.leg6 =  int(Calcdistance(self.port6.longitude,self.port6.latitude,self.port7.longitude,self.port7.latitude).distance)
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
       # print(self.portlist_inrange)
        #print([self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code])
        #print(self.portlist[3].code)



    def findbestroute(self):
        bestroute={}

        for index, eachcandidate in self.candidates.items():
            eachcandidate=list(eachcandidate)
            print('here we go',index,'  ',eachcandidate)
            if index<24: #process 5 leg routes--create route object but set genpermsflag to false as donot need permutations regenerated
                #with the route object pick of each airport at start ot leg (know its currency and use fuelling stragegy to evaluate cost keep track of costs
                pass
            else:#process six leg routes
                pass



x = Route('SXR', 'TNI', 'AGX', 'BLR', 'YYU', '747')
# print(x.candidates)

        # dist2home = self.routedist
        # for index, airport in enumerate(self.portlist): ##go through airport and build a set of reachable ports
        #
        #     legreach=0
        #     portsinrange={}
        #     RANGE=craft.range ###########################################################TODO##############
        #     for i in range(index:6):
        #     totallegdist=leg
















