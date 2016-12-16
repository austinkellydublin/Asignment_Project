from currencyrate import *
from __airport import *
from countrycurrency import *
from calculatedistance import *
from itertools import *  # use this baked in library to help generate permutations
from legdistances import *
from aircraft import *
from permroutes import *
from subroutes2 import*


class Cheapest():
    def __init__(self,candidates,max_range=7000):
        #print(candidates)
        cheapest_so_far=99999999999


        for routenumber, route in candidates.items():
            #print(route)


            if routenumber < 24:
                purchase_strategy=[]
                fuel_strategy=[]
                cost_fuel_bought = 0#total

                sub_routes= Subroutes(route,max_range).subroutes
                print('subroutes',sub_routes)
                airports = [Airport(route[0]), Airport(route[1]), Airport(route[2]), Airport(route[3]),
                            Airport(route[4]), Airport(route[5])]

                legs = Legdistances(route[0],route[1],route[2],route[3],route[4],route[5],).legslist
                legs.pop()
                #print(legs)###need the legs
                total_distance = legs[0] + legs[1] + legs[2] + legs[3] + legs[4]
                distance_travelled = 0


                for stopped_at_port in range( 5):#5 subroutes at max


                    sub_route = sub_routes[stopped_at_port]  #get the stop at ports self.inrange list
                    #check where we are on the itinary
                    if stopped_at_port == 0:##just stopped
                        distance_left = total_distance
                        current_fuel=0

                    else:
                        fuel_used = legs[stopped_at_port - 1]##fuel used on last leg is fuel travelling from last port
                        distance_travelled += fuel_used ## as a litre per km
                        current_fuel = current_fuel -fuel_used
                        distance_left = total_distance - distance_travelled

                    #start_leg = stopped_at_port  ##first leg index on subroutes is the same as the index of stopped at port
                    index_of_cheaper = stopped_at_port  ##initially set cheapest port in the subroute to BE the stopped at port until find otherwise
                    cheapest_rate = airports[stopped_at_port].currencyeurorate  ## initially set cheapest rate in the subroute to the stopped at ports

                   # print('about to enter     for idx2,aheadports in enumerate(subroute): ')
                   # print('subroute',sub_route)
                    for idx2, ahead_ports in enumerate(sub_route):
                            #print('subroute',sub_route)
                           # print('current stopped at airport index',stopped_at_port,'go in through idx loop line395  idx2 = ',idx2 )
                            ahead_ports_index = (stopped_at_port+1) + idx2  ##get the proper index of a port in subroute
                           # print('ahead airport index ',aheadportsindex,'aheadairport name',aheadports)
                            #print('aheadports indexs', aheadportsindex)
                            if (airports[ahead_ports_index].currencyeurorate <= cheapest_rate):  ##find next cheapest airport as will buy enough fuel to get to it
                                index_of_cheaper = ahead_ports_index
                                break
                    #print('cheaper rate',airports[ahead_ports_index].currencyeurorate,'at airport',airports[ahead_ports_index].code)# reset to index of cheapest port
                                #cheapest_rate = airports[ahead_ports_index].currencyeurorate#todo commente

                            # reset to index of cheapest port
                            # legidforcheapest = stopped_at_port + 1 + idx2
                    # print('in for x in range ..ateach to indexof cheaper')
                    ##TODO NOW BUY FUEL TO TRAVEL ONTO CHEAPER IF ONE IN RANGE ELSE TOP UP TO GET HOME OR TO END OF RANGE
                    if stopped_at_port == index_of_cheaper:##NO CHEAPER PORT IN RANGE BUT HOME IS WITHIN RANGE
                        if distance_left <= max_range and distance_left<=current_fuel:
                            fuel_to_buy = distance_left-current_fuel
                            cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                            current_fuel = current_fuel + fuel_to_buy
                            cost_fuel_bought += cost_to_buy
                            #print('AUSTIN')
                            if stopped_at_port == 0:
                                fuel_strategy = [fuel_to_buy]
                                purchase_strategy = [cost_to_buy]
                            else:
                                fuel_strategy = fuel_strategy + [fuel_to_buy]
                                purchase_strategy = purchase_strategy + [cost_to_buy]

                        elif distance_left>max_range:
                            fuel_to_buy = (max_range - current_fuel)  ##top up to max
                            cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                            current_fuel = current_fuel + fuel_to_buy
                            cost_fuel_bought += cost_to_buy

                            if stopped_at_port == 0:
                                fuel_strategy = [fuel_to_buy]
                                purchase_strategy = purchase_strategy + [cost_to_buy]
                            else:
                                fuel_strategy = fuel_strategy + [fuel_to_buy]
                                purchase_strategy = purchase_strategy + [cost_to_buy]
                    elif stopped_at_port != index_of_cheaper:
                        complete_distance_to_cheaper=0
                        for x in range(stopped_at_port,index_of_cheaper+1):
                            complete_distance_to_cheaper += legs[x]
                            #print('complete_distance_to_cheaper',complete_distance_to_cheaper)
                           # print('airports[stopped_at_port].currencyeurorate',airports[stopped_at_port].currencyeurorate)
                            fuel_to_buy =complete_distance_to_cheaper-current_fuel
                        #print(current_fuel)
                        #print(complete_distance_to_cheaper)
                        #print(fuel_to_buy)
                            cost_to_buy = (airports[stopped_at_port].currencyeurorate) * (fuel_to_buy)
                            current_fuel = current_fuel + fuel_to_buy
                            cost_fuel_bought += cost_to_buy

                        if stopped_at_port == 0:
                            fuel_strategy = [fuel_to_buy]
                            purchase_strategy = purchase_strategy + [cost_to_buy]
                        else:
                            fuel_strategy = fuel_strategy + [fuel_to_buy]
                            purchase_strategy = purchase_strategy + [cost_to_buy]




            if cost_fuel_bought < cheapest_so_far:
                cheapest_so_far=cost_fuel_bought
                self.cheapest_cost = int(cost_fuel_bought)
                self. cheapest_legs_distances = legs
                self. cheapest_distance = total_distance
                self.cheapest_route = route
                self.cheapest_purchase_strategy = [int(x) for x in purchase_strategy]
                self.cheapest_route_number=routenumber
                self.cheapest_fuel_strategy=fuel_strategy

        #print('legs',self.cheapest_legs_distances,'\n','purchases',self.cheapest_purchase_strategy,'fuel stategy',self.cheapest_fuel_strategy,'\n',self.cheapest_route,'\n',self.cheapest_route_number)

        #def main():
            #uncomment to check different starting permutations of same route to check consistency of algorithm
            #x = Route('BUS', 'DUB', 'AOC', 'LHR', 'TUF', '747')
            #y = Route('BUS', 'TUF', 'AOC', 'LHR', 'DUB', '747')
            #z = Route('LHR', 'DUB', 'BUS', 'AOC', 'TUF', '747')




def main():
    candidates = {0: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'],
              1: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'LHR'],
              2: ['LHR', 'DUB', 'AOC', 'BUS', 'TUF', 'LHR'],
              3: ['LHR', 'DUB', 'AOC', 'TUF', 'BUS', 'LHR'],
              4: ['LHR', 'DUB', 'TUF', 'BUS', 'AOC', 'LHR'],
              5: ['LHR', 'DUB', 'TUF', 'AOC', 'BUS', 'LHR'],
              6: ['LHR', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'],
              7: ['LHR', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'],
              8: ['LHR', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'],
              9: ['LHR', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'],
              10: ['LHR', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'],
              11: ['LHR', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'],
              12: ['LHR', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'],
              13: ['LHR', 'AOC', 'DUB', 'TUF', 'BUS', 'LHR'],
              14: ['LHR', 'AOC', 'BUS', 'DUB', 'TUF', 'LHR'],
              15: ['LHR', 'AOC', 'BUS', 'TUF', 'DUB', 'LHR'],
              16: ['LHR', 'AOC', 'TUF', 'DUB', 'BUS', 'LHR'],
              17: ['LHR', 'AOC', 'TUF', 'BUS', 'DUB', 'LHR'],
              18: ['LHR', 'TUF', 'DUB', 'BUS', 'AOC', 'LHR'],
              19: ['LHR', 'TUF', 'DUB', 'AOC', 'BUS', 'LHR'],
              20: ['LHR', 'TUF', 'BUS', 'DUB', 'AOC', 'LHR'],
              21: ['LHR', 'TUF', 'BUS', 'AOC', 'DUB', 'LHR'],
              22: ['LHR', 'TUF', 'AOC', 'DUB', 'BUS', 'LHR'],
              23: ['LHR', 'TUF', 'AOC', 'BUS', 'DUB', 'LHR'],
              24: ['LHR', 'DUB', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'],
              25: ['LHR', 'DUB', 'DUB', 'BUS', 'TUF', 'AOC', 'LHR'],
              26: ['LHR', 'DUB', 'DUB', 'AOC', 'BUS', 'TUF', 'LHR'],
              27: ['LHR', 'DUB', 'DUB', 'AOC', 'TUF', 'BUS', 'LHR'],
              28: ['LHR', 'DUB', 'DUB', 'TUF', 'BUS', 'AOC', 'LHR'],
              29: ['LHR', 'DUB', 'DUB', 'TUF', 'AOC', 'BUS', 'LHR'],
              30: ['LHR', 'DUB', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'],
              31: ['LHR', 'DUB', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'],
              32: ['LHR', 'DUB', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'],
              33: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'],
              34: ['LHR', 'DUB', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'],
              35: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'],
              36: ['LHR', 'DUB', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'],
              37: ['LHR', 'DUB', 'AOC', 'DUB', 'TUF', 'BUS', 'LHR'],
              38: ['LHR', 'DUB', 'AOC', 'BUS', 'DUB', 'TUF', 'LHR'],
              39: ['LHR', 'DUB', 'AOC', 'BUS', 'TUF', 'DUB', 'LHR'],
              40: ['LHR', 'DUB', 'AOC', 'TUF', 'DUB', 'BUS', 'LHR'],
              41: ['LHR', 'DUB', 'AOC', 'TUF', 'BUS', 'DUB', 'LHR'],
              42: ['LHR', 'DUB', 'TUF', 'DUB', 'BUS', 'AOC', 'LHR'],
              43: ['LHR', 'DUB', 'TUF', 'DUB', 'AOC', 'BUS', 'LHR'],
              44: ['LHR', 'DUB', 'TUF', 'BUS', 'DUB', 'AOC', 'LHR'],
              45: ['LHR', 'DUB', 'TUF', 'BUS', 'AOC', 'DUB', 'LHR'],
              46: ['LHR', 'DUB', 'TUF', 'AOC', 'DUB', 'BUS', 'LHR'],
              47: ['LHR', 'DUB', 'TUF', 'AOC', 'BUS', 'DUB', 'LHR'],
              48: ['LHR', 'DUB', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'],
              49: ['LHR', 'DUB', 'DUB', 'BUS', 'TUF', 'AOC', 'LHR'],
              50: ['LHR', 'DUB', 'DUB', 'AOC', 'BUS', 'TUF', 'LHR'],
              51: ['LHR', 'DUB', 'DUB', 'AOC', 'TUF', 'BUS', 'LHR'],
              52: ['LHR', 'DUB', 'DUB', 'TUF', 'BUS', 'AOC', 'LHR'],
              53: ['LHR', 'DUB', 'DUB', 'TUF', 'AOC', 'BUS', 'LHR'],
              54: ['LHR', 'DUB', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'],
              55: ['LHR', 'DUB', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'],
              56: ['LHR', 'DUB', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'],
              57: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'],
              58: ['LHR', 'DUB', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'],
              59: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR']}
    range=7000
    x= Cheapest(candidates,range)
    print(x.cheapest_route)
    print(x.cheapest_legs_distances)
    print(x.cheapest_cost)
if __name__ == '__main__':
    main()
