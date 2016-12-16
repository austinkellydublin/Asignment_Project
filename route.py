### route
#version 1.0
###Author Austin Kelly
'''This module analysis six legged and five legged alternative paths from a set of 5 airports when traveling in a given aircraft. it will calculate
the cheapest route and associated cost and distance travelled.
Route is the main class for the application and when called with five airports and a aircraft as perameters it initializes some instance variables and calls the
the Permroutes module to generate a collection of alternative routes for it to process. it sets a instance variable candidates to reference these alternative rountes
Then it goes through the alternative routes by calling the cleanup_candidate_routes method. once clean it uses these and for each stop on a route it generates a list of ports in range.
it then uses these routes and their subrotes to determine cheapest route via a call to the cheapest_route method'''

from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from itertools import *  # use this baked in library to help generate permutations
from legdistances import *
from aircraft import *
from permroutes import *
from cheapest import *
from cleanupcandidates import *



class Route:
    ###Route class will be  initiallized with 5 ports and a selected aircraft
    def __init__(self,port1,port2,port3,port4,port5,craft='777'):
        self.port1 = Airport(port1)#populate instance variable with values supplied by parameters
        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4= Airport(port4)
        self.port5 = Airport(port5)
        self.port6 = Airport(port1)## the first port is also the return port as its a round trip
        self.portlist=[self.port1.code,self.port2.code,self.port3.code,self.port4.code,self.port5.code,self.port6.code] # a convenience array of airports from submitted route
        self.craft = Aircraft(craft)##create an aircraft object from the craft parameter


        self.candidates= Permroutes(self.port1.code,self.port2.code,self.port3.code,self.port4.code,self.port5.code).candidates#permroutes generates the alternative paths and stores in a dictionary
        print(self.candidates)
        #  self.fuelstrategy = [] #will be filled in the cheapest_route method
       #  self.purchase_strategy = []  #holds purchase strategy filled in during cheapest_route method
       # # print(self.candidates)

        self.candidates_clean =Cleanup_candidate_routes(self.candidates).candidates
        print(self.candidates_clean)
        print('hello one')
        self.inrange=self.portsinrange() #for each alternative route we need a list of ports in range for each stop
        print(self.inrange)
        print('hello 2')
        #self.cheapest() # this will generate and store the cheapest route form all the different permutations
        self.cheapest=Cheapest(self.candidates_clean,self.inrange,self.candidates_legs)
        print(self.cheapest.cheapest_route)##as a list of codes
# craft= Aircraft('777')
# print('range  :',craft.range)

    #module permroutes has generated five hundred or so alternative routes but some of these are not viable as path given plane available
    # certain alternative paths have legs beyond fuel tank capacity or two stops are the same port so these are removed
    def cleanup_candidate_routes(self):####GET RID OF ROUTES THAT HAVE A LEG GREATER THAN FUEL TANK CAPACITIY or HAVE SAME PORT LISTED TWICE IN SUCCESSION
        todelete = [] ##used to store keys of all functions to delete
        maxfuelrange = self.craft.range  ## get fuel tanks range
        for routenumber, route in self.candidates.items(): #loop through list of alternative routes
            # get each candidate route
            if routenumber < 24:  #  6 airports in route and is a five legged journey
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist#the legdistance module just generates six leg journeys with last leg=0 for five ports
                legslist.pop()# remove the 6th leg for five leg journeys as this would be zero distance
                for leg in legslist:
                    if leg > maxfuelrange or leg==0:
                        todelete.append(routenumber)## add unsuitable route to list to delete
                        break  ####need break here or key could be appended a couple of times .....CAREFUL

            if routenumber >= 24:  ##then will have 7 airports and 6 legs same logic as above
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5], route[6]).legslist
                # print(candkey,'  ',legslist)
                for leg in legslist:
                    if leg > maxfuelrange or leg==0:
                        todelete.append(routenumber)
                        break
        #print(todelete) todo

        for each in todelete:
            #print('will delete',self.candidates[each])
            del self.candidates[each]
        return self.candidates

    # for each alternative route we need a list of ports in range for each stop
    def portsinrange(self):# FOR EACH ROUTE GENERATE A SET OF SUBROUTES WITH AIRPORT AHEAD WITHIN FLYING RANGE OF ANY GIVEN PORT FOR EACH HUB
        maxfuelrange = self.craft.range
        self.candidates_legs={}#this will hold all a list of leg distances for each alternative route referencable by the same key as the parent route for convenience and our sanity
        self.inrange = {} ##THIS WILL HOLD THE LIST OF SUBROUTES for each route and is keyed with the same key as the parent route for convenience and for our own sanity

        for routenumber, route in self.candidates.items(): ## process each route left remaining after clean up in the candidate routes dictionary
            aroutessubroutecollection=[]##an array to hold any given routes sub-routes

            if routenumber < 24:  # for five legged journeys generate the legs and populate the candidates_legs dictionary
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
                legsdist.pop()
                self.candidates_legs[routenumber]=legsdist
                for port in range(5):
                    fuel = maxfuelrange
                    aportssubroute = []
                    for leg in range(port, 5): #inner loop  will retake off from just landed port and see if can reach next station
                        if legsdist[leg]>fuel: #if distance to next port beyond reach append the subroute
                            aroutessubroutecollection.append(aportssubroute)
                            break #stop building the chain when a leg to far is reached
                        else:#
                            aportssubroute.append(route[leg + 1])# keeping building chain
                            #print('oringinal list',route,'could reach so append port to listforeachport',aportssubroute)
                            fuel= fuel - legsdist[leg]##adjust fuel before evaluate next leg
                            if leg==4: ##only a five leg journey so done last leg append and break
                                aroutessubroutecollection.append(aportssubroute)
                                break ##donot need this break but good to highlight logic
                self.inrange[routenumber]=aroutessubroutecollection

            if routenumber >= 24:  # for six  legged journeys same comments above apply
                legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5],route[6]).legslist
                self.candidates_legs[routenumber] = legsdist
                # print(route)
                # print('legsdist',legsdist)
                aportssubroute = []

                for port in range(6):
                    fuel = maxfuelrange  # from each port can start with full tank
                    # print('start fuel',fuel)
                    aportssubroute = []
                    for leg in range(port, 6):
                        # print(' at port', route[port]) #for each port will look at successive legs and see if can reach it
                        # print('leg',leg)
                        # build chain

                        if legsdist[leg] > fuel:

                            # print('aportssubroute',aportssubroute)
                            # print('entered break')
                            aroutessubroutecollection.append(aportssubroute)
                            break  # stop building the chain when a leg to far is reached

                        else:
                            aportssubroute.append(route[leg + 1])  # append port ahead
                            # print('oringinal list',route,'could reach so append port to listforeachport',aportssubroute)
                            fuel = fuel - legsdist[leg]

                            if leg == 5:
                                aroutessubroutecollection.append(aportssubroute)
                                break  # remove as donot need this break but good to highlight logic remove for production release
                self.inrange[routenumber] = aroutessubroutecollection
                return self.inrange,self.candidates_legs
               # print('routenumber',routenumber,'route', route)
                #print(self.candidates_legs[routenumber])
               # print('inrangeport', self.inrange[routenumber])





#     def cheapest(self):# this will generate and store the cheapest route form all the different permutations
#
#
#         cheapestsofar=9999999999999999999# set up some self documentingly named variables
#         costofroute=999999999999999999999
#         cheapestdistance=0
#         cheapestroutelist=[]
#
#         for routenumber, route in self.candidates.items():
#
#             if routenumber >= 24:  ##for routes with six legs
#                 ##set up some worker variables that are used later
#                 currentfuel = 0
#                 fueltobuy = 0
#                 fuelstrategy=[]
#                 purchase_strategy=[]
#                 legs = self.candidates_legs[routenumber] ##generate the six legs list
#                 subroutes = self.inrange[routenumber]  # a list of subroutes for each port stopped at en route
#                 # print('routenumber', routenumber, 'route', route)
#                 # print('subroutes for routenumber', routenumber, 'subroutes', subroutes)
#                 ###put airports on route into a convenience list
#                 airports = [Airport(route[0]), Airport(route[1]), Airport(route[2]), Airport(route[3]),
#                             Airport(route[4]), Airport(route[5]),Airport(route[6])]
#                 # print('airport index 0 airportcode',Airport(route[0]).code)
#                 costofthisroute = 9999999999999999999
#                 totaldistance = legs[0] + legs[1] + legs[2] + legs[3] + legs[4] + legs[5]
#                # print('totaldistance', totaldistance)
#                 distanceleft = totaldistance
#                 fuelboughtatthisroute = 0
#                 # print('entering subroutes')
#                 distancetravelled = 0
#                 costfuelbought = 0
#                 costtobuy =0
#
#                 for stopped_at_port in range(6): #for each leg of the journey
#
#                     subroute = subroutes[stopped_at_port]  ##get  subroute in range from a stopped at port
#                     if stopped_at_port == 0: #if at the very first port
#                         fuelused = 0
#                         distanceleft = totaldistance
#
#                     else:
#                         fuelused = legs[stopped_at_port - 1] ##fuel used up is fuel travelling from  from last port to current port
#                         distancetravelled += legs[stopped_at_port - 1]
#                         currentfuel -= fuelused
#                         distanceleft = totaldistance - distancetravelled
#
#                     startleg = stopped_at_port  ## the index of the first leg is the same as the port from which we are considering our refuel strategy
#                     indexofcheaper = stopped_at_port  ##initially set cheapest port( for any subroute )to be one just landed at
#                     cheapestrate = airports[stopped_at_port].currencyeurorate  ## initially set cheapest rate in the subroute to the stopped at ports
#                     ##tood# print('about to enter     for idx2,aheadports in enumerate(subroute): ')
#                     for idx2, aheadports in enumerate(subroute):  ## see if there is a cheaper port ahead within range cycle through ports looking for a cheaper one
#                         distancetocheaper = 0  ##will need to buy fuel to get to cheaper port
#
#
#                         aheadportsindex = stopped_at_port + 1 + idx2  ##get the 'proper index of a port in subroute
#                         # print('aheadports indexs', aheadportsindex)
#                         if  (airports[aheadportsindex].currencyeurorate <= cheapestrate):  ##find first cheapest airport as will buy enough fuel to get to it
#                             indexofcheaper = aheadportsindex  # reset to index of cheapest port
#                             cheapestrate = airports[aheadportsindex].currencyeurorate
#                             break
#                         else:
#                             pass
#
#                             # reset to index of cheapest port
#                             # legidforcheapest = stopped_at_port + 1 + idx2
#                     # print('in for x in range ..ateach to indexof cheaper')
#                     if stopped_at_port == indexofcheaper:## then there is no cheaper airport in range
#                         if distanceleft <= self.craft.range:
#                             fueltobuy = distanceleft - currentfuel
#                             costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                             currentfuel = currentfuel + fueltobuy
#                             costfuelbought += costtobuy
#                             if stopped_at_port == 0:
#                                 fuelstrategy = [fueltobuy]
#                                 purchase_strategy=[costtobuy]
#                             else:
#                                 fuelstrategy = fuelstrategy + [fueltobuy]
#                                 purchase_strategy= purchase_strategy + [costtobuy]
#                         else:  ## as distanceleft  > tank range and current is cheapest in range so max up to range
#                             fueltobuy = (self.craft.range - currentfuel)  ##top up to max
#                             costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                             currentfuel = currentfuel + fueltobuy
#                             if stopped_at_port == 0:
#                                 fuelstrategy = [fueltobuy]
#                                 purchase_strategy = [costtobuy]
#                             else:#append fuel and cost to their arrays
#                                 fuelstrategy = fuelstrategy + [fueltobuy]
#                                 purchase_strategy = purchase_strategy + [costtobuy]
#                     else:  ## there is a cheaper airport in reach so refuel at, so compute distance to it and top up to reach it
#                         for x in range(stopped_at_port, indexofcheaper+1):#add one as range stops short
#                             distancetocheaper += legs[x]
#                         fueltobuy = distancetocheaper - currentfuel
#                         costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                         currentfuel = currentfuel + fueltobuy
#                         costfuelbought += costtobuy
#                         if stopped_at_port == 0:
#                             fuelstrategy = [fueltobuy]
#                             purchase_strategy = [costtobuy]
#                         else:
#                             fuelstrategy = fuelstrategy + [fueltobuy]
#                             purchase_strategy = purchase_strategy + [costtobuy]
#
#                 if costfuelbought < cheapestsofar:
#                     cheapestsofar = costfuelbought
#                     cheapestroute = routenumber
#                     self.cheapest_distance = totaldistance
#                     cheapestroutelist = route
#                     self.costofcheapest = costfuelbought
#                     self.cheapestlegs = legs
#                     self.cheapest_cost = int(cheapestsofar)
#                     self.cheapest_route = cheapestroutelist
#                     self.fuelstrategy =fuelstrategy
#                     self.purchase_strategy = [int(x) for x in purchase_strategy]
#             if routenumber < 24:##for routes with five legs
#                 ##set up some worker variables used later
#                 purchase_strategy=[]
#                 fuelstrategy=[]
#                 currentfuel = 0
#                 fueltobuy = 0
#                 legs = self.candidates_legs[routenumber] ##generate the five legs list
#                 subroutes = self.inrange[routenumber]  # a list of subroutes for each port stopped at en route
#                 # print('routenumber', routenumber, 'route', route)
#                 # print('subroutes for routenumber', routenumber, 'subroutes', subroutes)
#                 airports = [Airport(route[0]), Airport(route[1]), Airport(route[2]), Airport(route[3]),
#                             Airport(route[4]), Airport(route[5])]
#                 # print('airport index 0 airportcode',Airport(route[0]).code)
#                 costofthisroute = 9999999999999999999
#                 totaldistance = legs[0] + legs[1] + legs[2] + legs[3] + legs[4]
#                # print('totaldistance', totaldistance)
#
#                 distanceleft = totaldistance
#                 # print('entering subroutes')
#                 distancetravelled = 0
#                 costfuelbought = 0
#                 costtobuy=0
#
#                 for stopped_at_port in range( 5): # for each leg of the journey
#                     subroute = subroutes[stopped_at_port]  ##load subroute in range for a stopped at port
#                     if stopped_at_port == 0:##at initial port
#                         fuelused = 0
#                         distanceleft = totaldistance
#
#                     else:
#                         fuelused = legs[stopped_at_port - 1]##fuel used is fuel travelling from last port
#                         distancetravelled += legs[stopped_at_port - 1] ## distanced travelled
#                         currentfuel -= fuelused
#                         distanceleft = totaldistance - distancetravelled
#                     # print('portindex',ateachport,'subroute',subroute)
#                     fuelboughtatthisport = 0
#                     ##initialize so variables for each iteration
#                     startleg = stopped_at_port  ##first leg index on subroutes is the same as the index of stopped at port
#                     indexofcheaper = stopped_at_port  ##initially set cheapest port in the subroute to BE the stopped at port until find otherwise
#                     cheapestrate = airports[
#                         stopped_at_port].currencyeurorate  ## initially set cheapest rate in the subroute to the stopped at ports
#
#                     # print('about to enter     for idx2,aheadports in enumerate(subroute): ')
#                     for idx2, aheadports in enumerate(subroute):## see if there is a cheaper port ahead within range
#                        # print('subroute',subroute)
#                        # print('current stopped at airport index',stopped_at_port,'go in through idx loop line395  idx2 = ',idx2 )
#                         distancetocheaper = 0##will buy fuel to get to cheaper port
#                         aheadportsindex = stopped_at_port + 1 + idx2  ##get the proper index of a port in subroute
#                        # print('ahead airport index ',aheadportsindex,'aheadairport name',aheadports)
#                         #print('aheadports indexs', aheadportsindex)
#                         if (airports[aheadportsindex].currencyeurorate <= cheapestrate):  ##find next cheapest airport as will buy enough fuel to get to it
#                             indexofcheaper = aheadportsindex  # reset to index of cheapest port
#                             cheapestrate = airports[aheadportsindex].currencyeurorate
#                             break
#                            # print('at airport',stopped_at_port,'but cheaper airport at index',aheadportsindex)
#
#                         else:
#                             pass
#                             # reset to index of cheapest port
#                             # legidforcheapest = stopped_at_port + 1 + idx2
#                     # print('in for x in range ..ateach to indexof cheaper')
#                     if stopped_at_port == indexofcheaper:##current aiport is cheapest in range so fill up to get home or max up
#                         if distanceleft <= self.craft.range:
#                             fueltobuy = distanceleft - currentfuel
#                             costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                             fueltobuy = distanceleft - currentfuel
#                             currentfuel = currentfuel + fueltobuy
#                             costfuelbought += costtobuy
#                             if stopped_at_port == 0:
#                                 fuelstrategy = [fueltobuy]
#                                 purchase_strategy = [costtobuy]
#                             else:
#                                 fuelstrategy = fuelstrategy + [fueltobuy]
#                                 purchase_strategy = purchase_strategy + [costtobuy]
#
#                         else: ##distance left  greater than fuel tank range   yet current airport is cheapest in range so max up to range
#                             fueltobuy = (self.craft.range - currentfuel)  ##top up to max
#                             costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                             currentfuel = currentfuel + fueltobuy
#                             if stopped_at_port == 0:
#                                 fuelstrategy = [fueltobuy]
#                                 purchase_strategy = purchase_strategy + [costtobuy]
#                             else:
#                                 fuelstrategy = fuelstrategy + [fueltobuy]
#                                 purchase_strategy = purchase_strategy + [costtobuy]
#                     else:## there is a cheaper airport in reach do fuel so compute distance to it and top up to reach it
#                         for x in range(stopped_at_port,indexofcheaper+1):
#                             distancetocheaper += legs[x]
#                         fueltobuy = distancetocheaper -currentfuel
#                         costtobuy = (airports[stopped_at_port].currencyeurorate) * (fueltobuy)
#                         currentfuel = currentfuel + fueltobuy
#                         costfuelbought += costtobuy
#                         if stopped_at_port == 0:
#                             fuelstrategy = [fueltobuy]
#                             purchase_strategy = purchase_strategy + [costtobuy]
#                         else:
#                             fuelstrategy = fuelstrategy + [fueltobuy]
#                             purchase_strategy = purchase_strategy + [costtobuy]
#                 if costfuelbought < cheapestsofar:
#                     cheapestsofar = costfuelbought
#                     cheapestroute = routenumber
#                     self.cheapest_distance = totaldistance
#                     cheapestroutelist = route
#                     self.costofcheapest = costfuelbought
#                     self.cheapestlegs = legs
#                     self.cheapest_cost = int(cheapestsofar)
#                     self.cheapest_route = cheapestroutelist
#                     self.fuelstrategy = fuelstrategy
#                     self.purchase_strategy = [int(x) for x in purchase_strategy]
#
def main():
    z = Route('LHR', 'DUB', 'BUS', 'AOC', 'TUF', '747')
    print('cost',z.cheapest_cost)
    print('routedetails',z.cheapest_route)
    print('route distance',z.cheapest_distance)
    print('fuel to buy strategy',z.fuelstrategy)
    print('legs distances',z.cheapestlegs)
    print('purchase strategy',z.purchase_strategy)
    print('self.costofcheapest',z.costofcheapest)

if __name__ == '__main__':
    main()


                # LDE	Tarbes	Fra
    main()
#     #uncomment to check different starting permutations of same route to check consistency of algorithm
#     #x = Route('BUS', 'DUB', 'AOC', 'LHR', 'TUF', '747')
#     #y = Route('BUS', 'TUF', 'AOC', 'LHR', 'DUB', '747')
















