### route
from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from itertools import *
from legdistances import *
from aircraft import *



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
        ##########################################self.cleanup_candidate_routes()
        self.cleanup_candidate_routes()
        self.portsinrange()
        self.cheapest()
# craft= Aircraft('777')
# print('range  :',craft.range)


    def cleanup_candidate_routes(self):####GET RID OF ROUTES THAT HAVE A LEG GREATER THAN FUEL TANK CAPACITIY
        todelete = []
        maxfuelrange = self.craft.range  ## get fuel tank range
        for routenumber, route in self.candidates.items():
            # get each candidate route
            if routenumber < 24:  # for five legged journeys
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
                legslist.pop()
                for leg in legslist:
                    if leg > maxfuelrange:
                        todelete.append(routenumber)
                        break  ####note if not here it will evaluate again for a second leg not valid therefore get routenumber appended a couple of times CAREFUL

            if routenumber >= 24:  ##then will have 7 airports and 6 legs
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5], route[6]).legslist
                # print(candkey,'  ',legslist)
                for leg in legslist:
                    if leg > maxfuelrange:
                        todelete.append(routenumber)
                        break
        #print(todelete) todo

        for each in todelete:
            #print('will delete',each)
            del self.candidates[each]
        #print(self.candidates) todo




    def portsinrange(self):# FOR EACH ROUTE GENERATE A SET OF SUBROUTES WITH AIRPORT AHEAD WITHIN FLYING RANGE OF ANY GIVEN PORT FOR EACH HUB

        self.candidates_legs={}
        todelete=[]
        maxfuelrange = self.craft.range
        self.inrange = {} ##THIS WILL HOLD THE LIST OF SUBROUTES KEYED WITH SAME KEY AS THE MASTER ROUTE
        for routenumber, route in self.candidates.items(): ## a route is a collection of airports todo call dictionary something info
            #todo want to collect dictionary of reachable ports and store them against routenumber
            aroutessubroutecollection=[]

            if routenumber < 24:  # for five legged journeys
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
                legsdist.pop()
                self.candidates_legs[routenumber]=legsdist
               # print(route)
                #print('legsdist',legsdist)
                aportssubroute=[] #todo kk

                for port in range(5):#todo for each port on a route build its itinary and store each itinary as an elemment
                    #print('just to know what route working for route number',routenumber ,route)

                   # print('at port',route[port])##check port name starting from
                    #prepare a list to be filled by second members clicks   second loop will add a entry on each of its clicks
                    #print('fresh list for  to fill',aportssubroute)
                    # list i in dictionary info_about will store the chain of  airports reachable from ith airport on a fuel tank
                    fuel = maxfuelrange #from each port can start with full tank
                    #print('start fuel',fuel)
                    aportssubroute = []
                    for leg in range(port, 5): #second loop to fill work list with reachable airportsfor any given port
                        #print(' at port', route[port]) #for each port will look at successive legs and see if can reach it
                        #print('leg',leg)
                        #build chain

                        if legsdist[leg]>fuel:
                            # append  port and its reachable chain into database about a rounte dictionary as finished building chain due to rest arenot reachable
                             # here is where you need append info to the dictionary about a route as are about to leave the  and may also need to update if reach end of loop
                            ##when port == 4  or maxed out about to finish with this route so updat its record
                            #print('aportssubroute',aportssubroute)
                            #print('entered break')
                            aroutessubroutecollection.append(aportssubroute)
                            break #stop building the chain when a leg to far is reached

                        else:#
                            aportssubroute.append(route[leg + 1])#append port ahead
                            #print('oringinal list',route,'could reach so append port to listforeachport',aportssubroute)
                            fuel= fuel - legsdist[leg]

                            if leg==4:
                                aroutessubroutecollection.append(aportssubroute)
                                break ##donot need this break but good to highlight logic

                self.inrange[routenumber]=aroutessubroutecollection

            if routenumber >= 24:  # for five legged journeys
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5],route[6]).legslist
                self.candidates_legs[routenumber] = legsdist
                # print(route)
                # print('legsdist',legsdist)
                aportssubroute = []

                for port in range(
                        6):  # todo for each port on a route build its itinary and store each itinary as an elemment
                    # print('just to know what route working for route number',routenumber ,route)

                    # print('at port',route[port])##check port name starting from
                    # prepare a list to be filled by second members clicks   second loop will add a entry on each of its clicks
                    # print('fresh list for  to fill',aportssubroute)
                    # list i in dictionary info_about will store the chain of  airports reachable from ith airport on a fuel tank
                    fuel = maxfuelrange  # from each port can start with full tank
                    # print('start fuel',fuel)
                    aportssubroute = []
                    for leg in range(port,
                                     6):  # second loop to fill work list with reachable airportsfor any given port
                        # print(' at port', route[port]) #for each port will look at successive legs and see if can reach it
                        # print('leg',leg)
                        # build chain

                        if legsdist[leg] > fuel:
                            # append  port and its reachable chain into database about a rounte dictionary as finished building chain due to rest arenot reachable
                            # here is where you need append info to the dictionary about a route as are about to leave the  and may also need to update if reach end of loop
                            ##when port == 4  or maxed out about to finish with this route so updat its record
                            # print('aportssubroute',aportssubroute)
                            # print('entered break')
                            aroutessubroutecollection.append(aportssubroute)
                            break  # stop building the chain when a leg to far is reached

                        else:  #
                            aportssubroute.append(route[leg + 1])  # append port ahead
                            # print('oringinal list',route,'could reach so append port to listforeachport',aportssubroute)
                            fuel = fuel - legsdist[leg]

                            if leg == 5:
                                aroutessubroutecollection.append(aportssubroute)
                                break  ##donot need this break but good to highlight logic
                self.inrange[routenumber] = aroutessubroutecollection
               # print('routenumber',routenumber,'route', route) todo
                #print(self.candidates_legs[routenumber]) todo
               # print('inrangeport', self.inrange[routenumber]) todo





    def cheapest(self):

        cheapestsofar=99999
        costofroute=999999999999999999999
        refuelstrategy=''
        cheapestdistance=0

        for routenumber, route in self.candidates.items():
            if routenumber < 24:
                currentfuel=0
                fueltobuy=0
                legs = self.candidates_legs[routenumber]
                subroutes = self.inrange[routenumber]  # a list of subroutes
                #print('routenumber', routenumber, 'route', route)
               # print('subroutes for routenumber', routenumber, 'subroutes', subroutes)
                airports=[Airport(route[0]),Airport(route[1]),Airport(route[2]),Airport(route[3]),Airport(route[4]),Airport(route[5])]
                #print('airport index 0 airportcode',Airport(route[0]).code)
                costofthisroute=9999999999999999999
                fuelstrategyatthisport=[]
                totaldistance=legs[0]+legs[1]+legs[2]+legs[3]+legs[4]
               # print('totaldistance',totaldistance)
                accumulated_distance=0
                distanceleft=totaldistance
                fuelboughtatthisroute=0
               # print('entering subroutes')
                distancetravelled=0
                fuelbought=0

                #as you visit each port see if you should buy fuel and how much
               # todo  self.craft.fuel exist use it
               # print('about to enter  for ateachport in range(5) : line 326')
                for ateachport in range(5) :#load in a given ports subroute nb ateachport is the index of port in mainroute and first port ahead of it is ateachport+1

                    subroute=subroutes[ateachport]##gets a list pulls a list from subroutes
                    if ateachport==0:
                        fuelused=0
                        distanceleft = totaldistance - distancetravelled

                    else:
                        fuelused=legs[ateachport-1]
                        distancetravelled+=legs[ateachport-1]
                        currentfuel-=fuelused
                        distanceleft=totaldistance-distancetravelled
                    #print('portindex',ateachport,'subroute',subroute)
                    fuelboughtatthisport=0
                    startleg=ateachport
                    indexofcheapest=ateachport
                    cheapestrate = airports[ateachport].currencyeurorate
                    legidforcheapest=startleg


                   # print('about to enter     for idx2,aheadports in enumerate(subroute): ')
                    for idx2,aheadports in enumerate(subroute):
                        distancetocheapest=0
                        ##thisairportindex=ateachport

                        aheadportsindex=ateachport+1+idx2
                        #print('aheadports indexs',aheadportsindex)
                        if (airports[aheadportsindex].currencyeurorate <= airports[ateachport].currencyeurorate)and (airports[aheadportsindex].currencyeurorate <= cheapestrate):
                            indexofcheapest=aheadportsindex
                            cheapestrate=airports[aheadportsindex].currencyeurorate
                            legidforcheapest=ateachport+1+idx2
                   # print('in for x in range ..ateach to indexof cheaper')
                    for x in range(ateachport,indexofcheapest):
                        distancetocheapest += legs[x]


                   # print('about to enter line 351')
                    if indexofcheapest==startleg:
                        if distanceleft< self.craft.range: #top up to reach end
                            fueltobuy=(cheapestrate)*(distanceleft-currentfuel)
                            currentfuel=currentfuel+fueltobuy
                            fuelbought += fueltobuy
                            break

                        else:
                            fueltobuy=cheapestrate* (self.craft.range-currentfuel)##top up to max
                            currentfuel=currentfuel+fueltobuy
                            fuelbought += fueltobuy


                    else:

                        fueltobuy= cheapestrate * (distancetocheapest-currentfuel) #top up to reach a cheap station
                        currentfuel=currentfuel+fueltobuy
                        fuelbought+=fueltobuy

                    #print('fuelboughtatthisport so far',fuelboughtatthisport)
                   # print('about to enter line 370')

                    #print('accumulated distance',accumulated_distance)
                   # print('distanceletf',distanceleft)
                #print('about to enter if fuelboughtatthisport< cheapestsofar:  line 374 ')
                if fuelbought< cheapestsofar:
                    cheapestsofar=fuelbought
                    cheapestroute=routenumber
                    cheapestdistance=totaldistance

            if routenumber >= 24:
                currentfuel = 0
                fueltobuy = 0
                legs = self.candidates_legs[routenumber]
                subroutes = self.inrange[routenumber]  # a list of subroutes
                # print('routenumber', routenumber, 'route', route)
                # print('subroutes for routenumber', routenumber, 'subroutes', subroutes)
                airports = [Airport(route[0]), Airport(route[1]), Airport(route[2]), Airport(route[3]),
                            Airport(route[4]), Airport(route[5]),Airport(route[6])]
                # print('airport index 0 airportcode',Airport(route[0]).code)
                costofthisroute = 9999999999999999999
                fuelstrategyatthisport = []
                totaldistance = legs[0] + legs[1] + legs[2] + legs[3] + legs[4]+ legs[5]
               # print('totaldistance', totaldistance)
                accumulated_distance = 0
                distanceleft = totaldistance
                fuelboughtatthisroute = 0
               # print('entering subroutes')
                distancetravelled = 0
                fuelbought = 0

                # as you visit each port see if you should buy fuel and how much
                # todo  self.craft.fuel exist use it
               # print('about to enter  for ateachport in range(5) : line 326')
                for ateachport in range(
                        6):  # load in a given ports subroute nb ateachport is the index of port in mainroute and first port ahead of it is ateachport+1

                    subroute = subroutes[ateachport]  ##gets a list pulls a list from subroutes
                    if ateachport == 0:
                        fuelused = 0
                        distanceleft = totaldistance - distancetravelled

                    else:
                        fuelused = legs[ateachport - 1]
                        distancetravelled += legs[ateachport - 1]
                        currentfuel -= fuelused
                        distanceleft = totaldistance - distancetravelled
                    # print('portindex',ateachport,'subroute',subroute)
                    fuelboughtatthisport = 0
                    startleg = ateachport
                    indexofcheapest = ateachport
                    cheapestrate = airports[ateachport].currencyeurorate
                    legidforcheapest = startleg

                   # print('about to enter     for idx2,aheadports in enumerate(subroute): ')
                    for idx2, aheadports in enumerate(subroute):
                        distancetocheapest = 0
                        ##thisairportindex=ateachport

                        aheadportsindex = ateachport + 1 + idx2
                       # print('aheadports indexs', aheadportsindex)
                        if (airports[aheadportsindex].currencyeurorate <= airports[ateachport].currencyeurorate) and (
                            airports[aheadportsindex].currencyeurorate <= cheapestrate):
                            indexofcheapest = aheadportsindex
                            cheapestrate = airports[aheadportsindex].currencyeurorate
                            legidforcheapest = ateachport + 1 + idx2
                    #print('in for x in range ..ateach to indexof cheaper')
                    for x in range(ateachport, indexofcheapest):  # todo add 1 or subtract 1
                        distancetocheapest += legs[x]


                    if indexofcheapest == startleg:
                        if distanceleft < self.craft.range:  # top up to reach end
                            fueltobuy = (cheapestrate) * (distanceleft - currentfuel)
                            currentfuel = currentfuel + fueltobuy
                            fuelbought += fueltobuy
                            break

                        else:
                            fueltobuy = cheapestrate * (self.craft.range - currentfuel)  ##top up to max
                            currentfuel = currentfuel + fueltobuy
                            fuelbought += fueltobuy


                    else:

                        fueltobuy = cheapestrate * (distancetocheapest - currentfuel)  # top up to reach a cheap station
                        currentfuel = currentfuel + fueltobuy
                        fuelbought += fueltobuy

                        # print('fuelboughtatthisport so far',fuelboughtatthisport)
                        # print('about to enter line 370')

                        # print('accumulated distance',accumulated_distance)
                        # print('distanceletf',distanceleft)
                # print('about to enter if fuelboughtatthisport< cheapestsofar:  line 374 ')
                if fuelbought < cheapestsofar:
                    cheapestsofar = fuelbought
                    cheapestroute = routenumber
                    cheapestdistance = totaldistance
        print('cheapestsofar',cheapestsofar)
        print('cheapestroutenumber',cheapestroute)
        print('cheapest distance',cheapestdistance)
        print('cheapest route',self.candidates[cheapestroute])

x = Route('BUS', 'TUF', 'DUB', 'LHR', 'AOC', '747')


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

















