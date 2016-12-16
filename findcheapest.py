##calculate leg distances
#version 1.0
###Author Austin Kelly
'''The file is used by the csv files i have endowed the class with extra properties for more complete file output if required'''
from permroutes import *
from cheapest2 import *
from aircraft import *
from csv import *

class Find_cheapest():
    def __init__(self,filename='test21.csv'):
        filename=filename
        results =[]
        try:
            with open(filename) as f:
                rows = csv.reader(f)  # returns a list like object--had problem with pycharm till i cast to a list
                list_a = list(rows)  # convert to a list proper
                route_table = []
                cheapest_routes = []
                for row in list_a[:]:
                    record = [row[0], row[1], row[2], row[3], row[4], row[5]]
                    route_table.append(record)
                for record in route_table:
                    candidates = Permroutes(record[0], record[1], record[2], record[3], record[4]).candidates
                    craft_range = Aircraft(record[5]).range
                    cheapest= Cheapest(candidates,craft_range)
                    self.cheapest_cost= cheapest.cheapest_cost
                    self.cheapest_legs_distances= cheapest.cheapest_legs_distances
                    self.cheapest_distance= cheapest.cheapest_distance
                    self.cheapest_route= cheapest.cheapest_route
                    self.cheapest_purchase_strategy= cheapest.cheapest_purchase_strategy
                    self.cheapest_fuel_strategy= cheapest.cheapest_fuel_strategy
                    cheapest_route=cheapest.cheapest_route
                    cheapest_routes.append(cheapest_route)
                with open('results_from_file_input.csv', 'w', encoding='utf-8', newline='') as  f:
                    writer = csv.writer(f)
                    for row in cheapest_routes:
                        wtiter.writerow(row)
        except:
            Logerrors('an error occurred during processing the findcheapest module whilst trying to open the file check file permissions')##writes to program log if problem occurs

def main():
    Find_cheapest('test21.csv')
if __name__ == '__main__':
    main()
#Find_cheapest()

# candidates = Permroutes(record[0], record[1], record[2], record[3], record[4])
# craft_range = Aircraft(record[5]).range
# cheapest_routes.append(Aircraft(candidates, craft_range))
