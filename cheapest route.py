from currencyrate import *
from __airport import  *
from countrycurrency import *
from calculatedistance import *
from itertools import *  # use this baked in library to help generate permutations
from legdistances import *
from aircraft import *
from permroutes import *

class Cheapest():

          def cheapest(self,route):# this will generate and store the cheapest route for all the different permutations
            candidates={0:['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'],1:['SNN','ORK','MAN','CDG''SIN','SNN']}
            ###TODO JUST SUPPLY ROUTE
            self.cheapest=9999999999999999999 #VARIABLES TO STORE CHEAPEST cost
            self.cheapest_distance=9999999999999999##total distance of cheapest route
            self.cheapest_route=[]##as a list of codes
            self.cheapest_purchase_strategy= [] #cost of each stage
            self.cheapest_route_number=9999999 #key number for entry in candidates dictionary
            self.cheapest_fuel_strategy=[]# how mmany litres to buy at each step
            self.cheapest_legs=[] # distance of each leg in route
            for routenumber, route in candidates.items():

                    purchase_strategy=[]
                    fuel_strategy=[]

                    current_fuel = 0
                    fuel_to_buy = 0
                    cost_to_buy = 0
                    cost_fuel_bought = 0#total

                    sub_routes= self.in_range[routenumber]
                    airports = [Airport(route[0]), Airport(route[1]), Airport(route[2]), Airport(route[3]),
                                Airport(route[4]), Airport(route[5])]

                    legs = self.candidates_legs[routenumber]  ###need the legs
                    total_distance = legs[0] + legs[1] + legs[2] + legs[3] + legs[4]
                    distance_travelled = 0
                    distance_left = total_distance


                    for stopped_at_port in range( 5): # for each leg of the journey
                        sub_route = sub_routes[stopped_at_port]  #get the stop at ports inrange list
                        if stopped_at_port == 0:##for the stopped at port
                            fuel_used = 0
                            distance_left = total_distance

                        else:
                            fuel_used = legs[stopped_at_port - 1]##fuel used on last leg is fuel travelling from last port
                            distance_travelled += fuel_used ## as a litre per km
                            current_fuel -= fuel_used
                            distance_left = total_distance - distance_travelled
                        # print('portindex',ateachport,'subroute',subroute)
                        fuel_bought_at_this_port = 0
                        #start_leg = stopped_at_port  ##first leg index on subroutes is the same as the index of stopped at port
                        index_of_cheaper = stopped_at_port  ##initially set cheapest port in the subroute to BE the stopped at port until find otherwise
                        cheapest_rate = airports[stopped_at_port].currencyeurorate  ## initially set cheapest rate in the subroute to the stopped at ports

                        # print('about to enter     for idx2,aheadports in enumerate(subroute): ')
                        #TODO NOW FIND CHEAPEST PORT IN RANGE
                        for idx2, ahead_ports in enumerate(sub_route):## see if there is a cheaper port ahead within range
                           # print('subroute',subroute)
                           # print('current stopped at airport index',stopped_at_port,'go in through idx loop line395  idx2 = ',idx2 )
                            distance_to_cheaper = 0##will buy fuel to get to cheaper port
                            ahead_ports_index = stopped_at_port + 1 + idx2  ##get the proper index of a port in subroute
                           # print('ahead airport index ',aheadportsindex,'aheadairport name',aheadports)
                            #print('aheadports indexs', aheadportsindex)
                            if (airports[ahead_ports_index].currencyeurorate <= cheapest_rate):  ##find next cheapest airport as will buy enough fuel to get to it
                                index_of_cheaper = ahead_ports_index  # reset to index of cheapest port
                                #cheapest_rate = airports[ahead_ports_index].currencyeurorate#todo commented out
                                break
                               # print('at airport',stopped_at_port,'but cheaper airport at index',aheadportsindex)

                            else:
                                pass
                                # reset to index of cheapest port
                                # legidforcheapest = stopped_at_port + 1 + idx2
                        # print('in for x in range ..ateach to indexof cheaper')
                        ##TODO NOW BUY FUEL TO TRAVEL ONTO CHEAPER IF ONE IN RANGE ELSE TOP UP TO GET HOME OR TO END OF RANGE
                        if stopped_at_port == index_of_cheaper:##NO CHEAPER PORT IN RANGE BUT HOME IS WITHIN RANGE
                            if distance_left <= self.craft.range:
                                fuel_to_buy = distance_left - current_fuel
                                cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                                current_fuel = current_fuel + fuel_to_buy
                                cost_fuel_bought += cost_to_buy
                                if stopped_at_port == 0:
                                    fuel_strategy = [fuel_to_buy]
                                    purchase_strategy = [cost_to_buy]
                                else:
                                    fuel_strategy = fuel_strategy + [fuel_to_buy]
                                    purchase_strategy = purchase_strategy + [cost_to_buy]

                            else: ##CHEAPEST IS FIRST PORT BUT NOT IN RANGE OF HOME SO MAX UP
                                fuel_to_buy = (self.craft.range - current_fuel)  ##top up to max
                                cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                                current_fuel = current_fuel + fuel_to_buy
                                cost_fuel_bought += cost_to_buy
                                if stopped_at_port == 0:
                                    fuel_strategy = [fuel_to_buy]
                                    purchase_strategy = purchase_strategy + [cost_to_buy]
                                else:
                                    fuel_strategy = fuel_strategy + [fuel_to_buy]
                                    purchase_strategy = purchase_strategy + [cost_to_buy]
                        else:## TODO THERE IS A CHEAPER PORT IN RANGE SO HAVE GET ENOUGH FUEL TO REACH IT
                            complete_distance_to_cheaper=0
                            for x in range(index_of_cheaper):
                                complete_distance_to_cheaper += leg[index_of_cheaper]

                            distance_to_cheaper = complete_distance_to_cheaper -distance_travelled
                            fuel_to_buy = distance_to_cheaper -current_fuel
                            cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                            current_fuel = current_fuel + fuel_to_buy
                            cost_fuel_bought += cost_to_buy
                            if stopped_at_port == 0:
                                fuel_strategy = [fuel_to_buy]
                                purchase_strategy = purchase_strategy + [costtobuy]
                            else:
                                fuel_strategy = fuel_strategy + [fuel_to_buy]
                                purchase_strategy = purchase_strategy + [cost_to_buy]
                    if cost_fuel_bought < cheapest_so_far:
                        self.cheapest = int(cost_fuel_bought)
                        self. cheapest_legs = legs
                        self. cheapest_distance = total_distance
                        self.cheapest_route = route
                        self.cheapest_purchase_strategy = [int(x) for x in purchase_strategy]
                        self.cheapest_route_number=routenumber
                        self.cheapest_fuel_strategy=fuel_strategy

                    print(self.cheapest_legs,self.cheapest,self.cheapest_fuel_strategy,self.cheapest_distance,self.cheapest_purchase_strategy,self.cheapest_route,self.cheapest_route_number)


        #def main():
            #uncomment to check different starting permutations of same route to check consistency of algorithm
            #x = Route('BUS', 'DUB', 'AOC', 'LHR', 'TUF', '747')
            #y = Route('BUS', 'TUF', 'AOC', 'LHR', 'DUB', '747')
            #z = Route('LHR', 'DUB', 'BUS', 'AOC', 'TUF', '747')

