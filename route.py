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
        self.cleanup_candidate_routes()
        self.portsinrange()
# craft= Aircraft('777')
# print('range  :',craft.range)


    def cleanup_candidate_routes(self):
        todelete = []
        maxfuelrange = 7500 #self.craft.range  ## get fuel tank range
        for routenumber, route in self.candidates.items():
            # get each candidate route
            if routenumber < 24:  # for five legged journeys
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
                legslist.pop()
                for leg in legslist:
                    if leg > maxfuelrange:
                        todelete.append(routenumber)
                        break  ####note if not here it will evaluate again for a second leg not valid therefore get routenumber appended a couple of times CAREFUL

        #print(todelete)

            if routenumber >= 24:  ##then will have 7 airports and 6 legs
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5], route[6]).legslist
                # print(candkey,'  ',legslist)
                for leg in legslist:
                    if leg > maxfuelrange:
                        todelete.append(routenumber)
                        break
        print(todelete)

        for each in todelete:
            #print('will delete',each)
            del self.candidates[each]
        print(self.candidates)




    def portsinrange(self):
        candidates_legs={}
        todelete=[]
        maxfuelrange = self.craft.range
        newdictionary_routenumber_listoflistforallitsports = {}
        for routenumber, route in self.candidates.items(): ## a route is a collection of airports todo call dictionary something info
            #todo want to collect dictionary of reachable ports and store them against routenumber
            arouteslistoflists=[]

            if routenumber < 24:  # for five legged journeys
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
                legsdist.pop()
                candidates_legs[routenumber]=legsdist
                #print(route)
                #print('legsdist',legsdist)


                for port in range(5):#todo for each port on a route build its itinary and store each itinary as an elemment
                    #print('just to know what route working for route number',routenumber ,route)
                    startnumber=port #read in port to start from
                    #print('at port',route[port])##check port name starting from
                    listforeachport=[]#prepare a list to be filled by second members clicks   second loop will add a entry on each of its clicks
                    #print('fresh list for  to fill',listforeachport)
                    # list i in dictionary info_about will store the chain of  airports reachable from ith airport on a fuel tank
                    fuel = maxfuelrange #from each port can start with full tank
                    #print('start fuel',fuel)
                    for leg in range(port, 5): #second loop to fill work list with reachable airportsfor any given port
                        #print(' at port', route[port]) #for each port will look at successive legs and see if can reach it
                        #print('leg',leg)
                        #build chain
                        if legsdist[leg]>fuel:
                            # append  port and its reachable chain into database about a rounte dictionary as finished building chain due to rest arenot reachable
                             # here is where you need append info to the dictionary about a route as are about to leave the  and may also need to update if reach end of loop
                            ##when port == 4  or maxed out about to finish with this route so updat its record
                            #print('workerlist',listforeachport)
                            #print('entered break')
                            arouteslistoflists.append(listforeachport)
                            break #stop building the chain when a leg to far is reached

                        else:# else add the next aiport to the chain, then proceed to examine the next leg
                           # print(cand[k+1])
                            #info_about[i].append(cand[k + 1])

                            listforeachport.append(route[leg + 1])
                            #print('oringinal list',route,'could reach so append port to listforeachport',listforeachport)
                            fuel= fuel - legsdist[leg]
                            #print('new fuel',fuel)
                            if leg==4:
                                arouteslistoflists.append(listforeachport)

                                # todo append  port and its reachable chain into database about a rounte dictionary as finished building chain due to rest arenot reachable
                                #todo where and how do we update database before we leave loop port:its reachable list
                                ##todo when port == 4  or maxed out about to finish with this route so updat its record
                                break ##donot need this break but good to highlight logic


                    newdictionary_routenumber_listoflistforallitsports[routenumber]=arouteslistoflists

            if routenumber >=24 :  # for five legged journeys
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5],route[6]).legslist
                candidates_legs[routenumber] = legsdist
                # print(route)
                # print('legsdist',legsdist)


                for port in range(6):  #  for each port on a route build its itinary and store each itinary as an elemment
                    listforeachport = []  # prepare a list to be filled by second members clicks   second loop will add a entry on each of its clicks
                    fuel = maxfuelrange  # from each port can start with full tank
                    for leg in range(port, 6):  # second loop to fill work list with reachable airportsfor any given port
                        if legsdist[leg] > fuel:
                            arouteslistoflists.append(listforeachport)
                            break  # stop building the chain when a leg to far is reached
                        else:  # else add the next aiport to the chain, then proceed to examine the next leg
                            listforeachport.append(route[leg + 1])
                            fuel = fuel - legsdist[leg]
                            # print('new fuel',fuel)
                            if leg == 5:
                                arouteslistoflists.append(listforeachport)
                                break  ##donot need this break but good to highlight logic

                    newdictionary_routenumber_listoflistforallitsports[routenumber] = arouteslistoflists

        #print('for route',self.candidates[0],'at each station can reach following')
        #print(newdictionary_routenumber_listoflistforallitsports[0])
        #print('for route', self.candidates[26], 'at each station can reach following')
        #print(newdictionary_routenumber_listoflistforallitsports[26])


#### TODO HAVE ALL THE INFO I NEED   CANDIDATES,PORTSREACHABLE,PRICES,CANDIDATESLEGS


x = Route('TXL', 'SFO', 'DUB', 'LHR', 'TLS', '747')
# LDE	Tarbes	France
# TLS	Toulouse	France
# TUF	Tours	France
# BUS	Batumi	Georgia
# KUT	Kutaisi	Georgia
# TBS	Tbilisi	Georgia
# AOC	Altenburg	Germany
# SXF	Berlin	Germany
# TXL	Berlin	Germany
# BWE
# print(x.candidates)


        # dist2home = self.routedist
        # for index, airport in enumerate(self.portlist): ##go through airport and build a set of reachable ports
        #
        #     legreach=0
        #     portsinrange={}
        #     RANGE=craft.range ###########################################################TODO##############
        #     for i in range(index:6):
        #     totallegdist=leg
















