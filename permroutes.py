##calculate leg distances
#version 1.0
###Author Austin Kelly
#### this module will generate 5 and 6 leg permutations

from __airport import  *
from calculatedistance import *
from itertools import *
from legdistances import *


class Permroutes(): #when called the constructor will generate alternative five and six leg paths using the arguments supplied to the constructor
    def __init__(self,port1,port2,port3,port4,port5):
        self.port1 = Airport(port1)
        self.port2 = Airport(port2)
        self.port3 = Airport(port3)
        self.port4 = Airport(port4)
        self.port5 = Airport(port5)
        self.candidates={}## this will be populated wit the alternative candidate routes
        self.permit()



    def permit(self):##this uses the itertools permutation method to generate the alternative routes
        candidates = {}
        route5 = list(permutations([self.port2.code, self.port3.code, self.port4.code, self.port5.code]))
       # print(route5)
        route6a = list(
            permutations([self.port2.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code]))
        #print(route6a)
        route6b = list(
            permutations([self.port2.code, self.port3.code, self.port3.code, self.port4.code, self.port5.code]))
       # print(route6b)
        route6c = list(
            permutations([self.port2.code, self.port3.code, self.port4.code, self.port4.code, self.port5.code]))
        # print(route6c)
        route6d = list(
            permutations([self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port5.code]))
       # print(route6d)
       # print(len(route6a))# check number of permutations

        for index, eachlist in (enumerate(route5)): ##now we have to put the home port to the front and end of the generated alternative routes
            candidates[index] = [self.port1.code] + list(eachlist) + [self.port1.code]
        for index, eachlist in (enumerate(route6a)):
            candidates[24 + index] = [self.port1.code] + list(eachlist) + [self.port1.code]
        for index, eachlist in (enumerate(route6b)):
            candidates[144 + index] = [self.port1.code] + list(eachlist) + [self.port1.code]
        for index, eachlist in (enumerate(route6c)):
            candidates[264 + index] = [self.port1.code] + list(eachlist) + [self.port1.code]
        for index, eachlist in (enumerate(route6d)):
            candidates[384 + index] = [self.port1.code] + list(eachlist) + [self.port1.code]
        self.candidates = candidates  # these are the possible routes as lists in a dictionary called candidates
        #print(self.candidates)


def main():
    x = Permroutes('LHR', 'DUB', 'BUS', 'AOC', 'TUF')
    print(x.candidates)
if __name__ == '__main__':
    main()
