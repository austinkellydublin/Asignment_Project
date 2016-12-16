##Terminal_app.py
#version 1.01
###Author Austin Kelly
'''this module presents a command line interface to the user for the app'''
from cheapest2 import *
from permroutes import *


##from route import *

def main():
    try:## gather input from the user
        print('******* Terminal airport app Beta Version 1.0 by Austin Kelly ********* ')
        port1=input('************* please input the starting airport\'s code in uppercase e.g.LHR : ')
        port2 = input('*************please input the second airport\'s code in uppercase e.g.DUB : ')
        port3 = input('*************please input the third airport\'s code in uppercase e.g.BUS: ')
        port4 = input('*************please input the fourth airport\'s code in uppercase e.g. AOC : ')
        port5 = input('*************please input the fifth and final airport\'s code in uppercase e.g.TUF : ')
        airportlista= [port1,port2,port3,port4,port5] ## put in a convenience wrapper
        for port_idx in airportlista: # loop through input and clean it or report error back to user
            try:
                if len(port_idx) != 3:
                    raise Exception()
            except:
                print('Check your inputs and the make sure the files are all in current directory and complete')
                yesno = input('Would you like to try again? enter YES or NO  :')
                yesno = yesno.upper()
                if yesno == 'YES':
                    main()
                else:
                    print('\n\n!!!!!!!Warning the program would have shut down i have restarted for demo purposes!!!!!!!')
                    #exit()
                    main()
            port_idx=port_idx.upper()
        aircraft = input('please input the aircraft model e.g. 747  ; ') # get aircraft from user
        print('Please wait. This will take few MINUTES as we have to run a lot of permutations')
        candidates = Permroutes(port1,port2,port3,port4,port5).candidates
        craft_range = Aircraft(aircraft).range
        cheapest = Cheapest(candidates, craft_range)
        print('cheapest route is ',cheapest.cheapest_route)

        print('cheapest cost is ',cheapest.cheapest_cost)

        print('the legs distances are',cheapest.cheapest_legs_distances)
        print('cheapest distance is ',cheapest.cheapest_distance)

        print('cheapest purchase strategy is ' ,cheapest.cheapest_purchase_strategy)
        print('cheapest fuel strategey is ',cheapest.cheapest_fuel_strategy)
    except: ## deal with user invalid input
        print('Check your inputs and the make sure the files are all in current directory and complete')
        yesno=input('Would you like to try again? enter YES or NO')
        yesno=yesno.upper()
        if yesno == 'Yes' :
            main()
        else:
            print('\n\n!!!!!!!Warning the program would have shut down i have restarted for demo purposes!!!!!!!')
            # exit()
            main()

if __name__ == '__main__':
    main()




