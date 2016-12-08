### route
from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from aircraft import *
from itertools import *
from legdistances import *


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
        #self.calclegs()
        self.portlist=[self.port1,self.port2,self.port3,self.port4,self.port5,self.port6,self.port7]
        self.craft = Aircraft(craft)
        self.portlookup={port1: self.port1,port2: self.port2,port3: self.port3,port4: self.port4,port5: self.port5}
       # print(self.portlookup)
       # print('CHECK CODE LOOK UP', self.portlookup['TNI'])
       # print(self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code)
       # print('aircratf model :',self.craft.model)
        #print('range  :',self.craft.range)
        if self.genperms==True :
            candidates={}
            route5 = list(permutations([self.port2.code,self.port3.code,self.port4.code,self.port5.code]))
           # print(route5)
            route6a = list(permutations([self.port2.code,self.port2.code, self.port3.code, self.port4.code, self.port5.code]))
            #print(route6a)
            route6b = list(permutations([self.port2.code,self.port3.code ,self.port3.code, self.port4.code, self.port5.code]))
           # print(route6b)
            route6c = list(permutations([self.port2.code, self.port3.code, self.port4.code,self.port4.code, self.port5.code]))
           # print(route6c)
            route6d = list(permutations([self.port2.code,self.port3.code, self.port4.code,self.port5.code,self.port5.code]))
           # print(route6d)
            # print(len(route6a)) check number of permutations

            for index, eachlist in (enumerate(route5)): #  will set off and return to home to build a complete route from each permutation
                candidates[index] =[port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6a)):
                candidates[24+index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6b)):
                candidates[144 + index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6c)):
                candidates[264 + index] = [port1] + list(eachlist) + [port1]
            for index, eachlist in (enumerate(route6d)):
                candidates[384 + index] = [port1] + list(eachlist) + [port1]
                self.candidates=candidates #these are the possible routes
            #print(self.candidates)
            #print(len(self.candidates))
           # self.portsinrange()
        else:pass
        #self.findbestroute()


    # def calclegs(self):
    #     self.leg1 =  int(Calcdistance(self.port1.longitude, self.port1.latitude,self.port2.longitude,self.port2.latitude).distance)
    #     self.leg2 =  int(Calcdistance(self.port2.longitude,self.port2.latitude,self.port3.longitude,self.port3.latitude).distance)
    #     self.leg3 =  int(Calcdistance(self.port3.longitude,self.port3.latitude,self.port4.longitude,self.port4.latitude).distance)
    #     self.leg4 =  int(Calcdistance(self.port4.longitude,self.port4.latitude,self.port5.longitude,self.port5.latitude).distance)
    #     self.leg5 =  int(Calcdistance(self.port5.longitude,self.port5.latitude,self.port6.longitude,self.port6.latitude).distance)
    #     self.leg6 =  int(Calcdistance(self.port6.longitude,self.port6.latitude,self.port7.longitude,self.port7.latitude).distance)
    #     self.legslist = [self.leg1, self.leg2, self.leg3 ,self.leg4, self.leg5, self.leg6]
    #
    #     self.routedist = (self.leg1 +  self.leg2 + self.leg3 + self.leg4 + self.leg5 + self.leg6 )

       # print('leg1', self.leg1,'  leg2', self.leg2,'  leg3', self.leg3,'  leg4', self.leg4,'  leg5', self.leg5,'  leg6', self.leg6)
        #print(self.routedist)
        self.portsinrange()
# craft= Aircraft('777')
# print('range  :',craft.range)


    def portsinrange(self):
        ##at each airport will need a list of airports within fuel tank range these will be stored in a dictionary portlist_inrange
        maxfuelrange= self.craft.range ## get fuel tank range
        portlist_inrange = {}
        for index, portlista in self.candidates.items(): #get each candidate route
            portlista = list(portlista)
           # print('here we go',index,'  ',portlista)
            if index<24: #for five legged journeys
                legslist = Legdistances(portlista[0],portlista[1],portlista[2],portlista[3],portlista[4],portlista[5]).legslist
                for i in range(0,5): # for  all ports up to last port but excluding it
                   # print('i', i)
                    portlist_inrange[i]=[] # setup parent list for children lists
                    rangelist = [] #set up child list
                    fuel = maxfuelrange
                    for k in range(i,5): # for sucessive ports there are less ports ahead
                       # print('k', k)
                        if fuel >= legslist[k]: #
                            rangelist.append(portlista[k+1]) #add port at end of leg as reachable
                            portlist_inrange[i] = rangelist #update parent list with amended child
                            fuel -= legslist[k]   # adjust fuel in algorithm else will evaluate other legs and include them if the pass criteria
                        else:
                            break # if any port out of range then no sense in evaluating more distant ports so set fuel to zero

                        # update list of reachable ports for a given airport
                print(index,'\n\n',portlista,'\n',portlist_inrange,'\n\n')
            if index>=24:##then will have 7 airports and 6 legs
                legslist = Legdistances(portlista[0], portlista[1], portlista[2], portlista[3], portlista[4],
                                        portlista[5],portlista[6]).legslist
                for i in range(0, 6):  # for  all ports up to last port
                   # print('i', i)
                    portlist_inrange[i] = []
                    rangelist = []
                    fuel = maxfuelrange
                    for k in range(i, 6):  # for legs ahead each port
                       # print('k', k)
                        if fuel >= legslist[k]:
                            rangelist.append(portlista[k + 1])
                            portlist_inrange[i] = rangelist
                            fuel -= legslist[k]  # even route out of range must adjust fuel in algorithm else will evaluate other legs and include them if the pass criteria
                        else:
                            break
                print(index, '\n\n', portlista, '\n', portlist_inrange, '\n\n')


                    #else: break
       # print(self.portlist_inrange)
        #print([self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code])
        #print(self.portlist[3].code)



    # def findbestroute(self):
    #     bestroute={}
    #
    #     for index, eachcandidate in self.candidates.items():
    #         eachcandidate = list(eachcandidate)
    #         print('here we go',index,'  ',eachcandidate)
    #         if index<24:#process 5 leg routes

             #   eachcandidate=

               ## --create route object but set genpermsflag to false as donot need permutations regenerated//DONOT NEED THIS IF I USE A LOOKUP DICT
                #with the route object pick of each airport at start ot leg (know its currency and use fuelling stragegy to evaluate cost keep track of costs
        #         pass
        #     else:#process six leg routes
        #         pass
        # pass



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
















