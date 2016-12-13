##Terminal_app.py
#version 1.0
###Author Austin Kelly
### this module


from route import *

def main():
    print('Welcome, to the pleasure dome.')
    port1=input('please input the starting airport\'s code in uppercase e.g.LHR : ')
    port2 = input('please input the second airport\'s code in uppercase e.g.DUB : ')
    port3 = input('please input the third airport\'s code in uppercase e.g.BUS: ')
    port4 = input('please input the fourth airport\'s code in uppercase e.g. AOC : ')
    port5 = input('please input the fifth and final airport\'s code in uppercase e.g.TUF : ')
    aircraft = input('please input the aircraft model e.g. 747  ; ')
    print('This will take few moments as we have to run alot of permutations, go have a beer and come back in five')
    print ('The best route is', Route(port1,port2,port3,port4,port5,aircraft).cheapest_route)



if __name__ == '__main__':
    main()

'LHR', 'DUB', 'BUS', 'AOC', 'TUF', '747'



