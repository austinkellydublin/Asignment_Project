##calculate leg distances
#version 1.0
###Author Austin Kelly
'''this module's purpose is to receive a set dictionary of candidates and clean out any candidates that have zero distance between to consecutive members as this state will
 already be captured in the five leg candidates and it also clears out any alternatives that have a stage beyond the reach of the planes range.'''

from legdistances import *
class Cleanup_candidate_routes():# initialization is via two parameters dictionary with all the alternative paths generated and the range of te aircraft

    def __init__(self,candidates,craft_range):  ####GET RID OF ROUTES THAT HAVE A LEG GREATER THAN FUEL TANK CAPACITIY or HAVE SAME PORT LISTED TWICE IN SUCCESSION

        todelete = []  ##used to store keys of all functions to delete
        maxfuelrange = craft_range  ## get fuel tanks range
        for routenumber, route in candidates.items():  # loop through list of alternative routes
            # get each candidate route
            if routenumber < 24:  # 6 airports in route and is a five legged journey
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[
                    5]).legslist  # the legdistance module just generates six leg journeys with last leg=0 for five ports
                legslist.pop()
               # print('leglist',legslist)
                # remove the 6th leg for five leg journeys as this would be zero distance
                for leg in legslist:
                    if leg > maxfuelrange or leg == 0:
                        todelete.append(routenumber)  ## add unsuitable route to list to delete
                        break  ####need break here or key could be appended a couple of times .....CAREFUL

            if routenumber >= 24:  ##then will have 7 airports and 6 legs same logic as above
                legslist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5], route[6]).legslist
                # print(candkey,'  ',legslist)
                for leg in legslist:
                    if leg > maxfuelrange or leg == 0: #put any candidates that are beyond fuel tank range or have a zero distance between consecutive stops in deletable items dictionay
                        todelete.append(routenumber)
                        break
        #print('to delete',todelete)

        for each in todelete:
            # print('will delete',self.candidates[each])
            del candidates[each]# delete item in the delete dictionary from the candidates dictionary assign cleaned alternative to a candidates attribute
        self.candidates=candidates
       # print('self.candidates',self.candidates)


def main():##this is a test fuction that should return list below
    candidates = {0: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'], 1: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'LHR'],
                  2: ['LHR', 'DUB', 'AOC', 'BUS', 'TUF', 'LHR'], 3: ['LHR', 'DUB', 'AOC', 'TUF', 'BUS', 'LHR'],
                  4: ['LHR', 'DUB', 'TUF', 'BUS', 'AOC', 'LHR'], 5: ['LHR', 'DUB', 'TUF', 'AOC', 'BUS', 'LHR'],
                  6: ['LHR', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'], 7: ['LHR', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'],
                  8: ['LHR', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'], 9: ['LHR', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'],
                  10: ['LHR', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'], 11: ['LHR', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'],
                  12: ['LHR', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'], 13: ['LHR', 'AOC', 'DUB', 'TUF', 'BUS', 'LHR'],
                  14: ['LHR', 'AOC', 'BUS', 'DUB', 'TUF', 'LHR'], 15: ['LHR', 'AOC', 'BUS', 'TUF', 'DUB', 'LHR'],
                  16: ['LHR', 'AOC', 'TUF', 'DUB', 'BUS', 'LHR'], 17: ['LHR', 'AOC', 'TUF', 'BUS', 'DUB', 'LHR'],
                  18: ['LHR', 'TUF', 'DUB', 'BUS', 'AOC', 'LHR'], 19: ['LHR', 'TUF', 'DUB', 'AOC', 'BUS', 'LHR'],
                  20: ['LHR', 'TUF', 'BUS', 'DUB', 'AOC', 'LHR'], 21: ['LHR', 'TUF', 'BUS', 'AOC', 'DUB', 'LHR'],
                  22: ['LHR', 'TUF', 'AOC', 'DUB', 'BUS', 'LHR'], 23: ['LHR', 'TUF', 'AOC', 'BUS', 'DUB', 'LHR'],
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
                  59: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'],
                  60: ['LHR', 'DUB', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'],
                  }

    x=Cleanup_candidate_routes(candidates,7000).candidates
    print('clean candidates',x)
if __name__ == '__main__':
    main()
##result of test should be the following clean candidates {0: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'LHR'], 1: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'LHR'], 2: ['LHR', 'DUB', 'AOC', 'BUS', 'TUF', 'LHR'], 3: ['LHR', 'DUB', 'AOC', 'TUF', 'BUS', 'LHR'], 4: ['LHR', 'DUB', 'TUF', 'BUS', 'AOC', 'LHR'], 5: ['LHR', 'DUB', 'TUF', 'AOC', 'BUS', 'LHR'], 6: ['LHR', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'], 7: ['LHR', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'], 8: ['LHR', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'], 9: ['LHR', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'], 10: ['LHR', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'], 11: ['LHR', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'], 12: ['LHR', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'], 13: ['LHR', 'AOC', 'DUB', 'TUF', 'BUS', 'LHR'], 14: ['LHR', 'AOC', 'BUS', 'DUB', 'TUF', 'LHR'], 15: ['LHR', 'AOC', 'BUS', 'TUF', 'DUB', 'LHR'], 16: ['LHR', 'AOC', 'TUF', 'DUB', 'BUS', 'LHR'], 17: ['LHR', 'AOC', 'TUF', 'BUS', 'DUB', 'LHR'], 18: ['LHR', 'TUF', 'DUB', 'BUS', 'AOC', 'LHR'], 19: ['LHR', 'TUF', 'DUB', 'AOC', 'BUS', 'LHR'], 20: ['LHR', 'TUF', 'BUS', 'DUB', 'AOC', 'LHR'], 21: ['LHR', 'TUF', 'BUS', 'AOC', 'DUB', 'LHR'], 22: ['LHR', 'TUF', 'AOC', 'DUB', 'BUS', 'LHR'], 23: ['LHR', 'TUF', 'AOC', 'BUS', 'DUB', 'LHR'], 30: ['LHR', 'DUB', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'], 31: ['LHR', 'DUB', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'], 32: ['LHR', 'DUB', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'], 33: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'], 34: ['LHR', 'DUB', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'], 35: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'], 36: ['LHR', 'DUB', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR'], 37: ['LHR', 'DUB', 'AOC', 'DUB', 'TUF', 'BUS', 'LHR'], 38: ['LHR', 'DUB', 'AOC', 'BUS', 'DUB', 'TUF', 'LHR'], 39: ['LHR', 'DUB', 'AOC', 'BUS', 'TUF', 'DUB', 'LHR'], 40: ['LHR', 'DUB', 'AOC', 'TUF', 'DUB', 'BUS', 'LHR'], 41: ['LHR', 'DUB', 'AOC', 'TUF', 'BUS', 'DUB', 'LHR'], 42: ['LHR', 'DUB', 'TUF', 'DUB', 'BUS', 'AOC', 'LHR'], 43: ['LHR', 'DUB', 'TUF', 'DUB', 'AOC', 'BUS', 'LHR'], 44: ['LHR', 'DUB', 'TUF', 'BUS', 'DUB', 'AOC', 'LHR'], 45: ['LHR', 'DUB', 'TUF', 'BUS', 'AOC', 'DUB', 'LHR'], 46: ['LHR', 'DUB', 'TUF', 'AOC', 'DUB', 'BUS', 'LHR'], 47: ['LHR', 'DUB', 'TUF', 'AOC', 'BUS', 'DUB', 'LHR'], 54: ['LHR', 'DUB', 'BUS', 'DUB', 'AOC', 'TUF', 'LHR'], 55: ['LHR', 'DUB', 'BUS', 'DUB', 'TUF', 'AOC', 'LHR'], 56: ['LHR', 'DUB', 'BUS', 'AOC', 'DUB', 'TUF', 'LHR'], 57: ['LHR', 'DUB', 'BUS', 'AOC', 'TUF', 'DUB', 'LHR'], 58: ['LHR', 'DUB', 'BUS', 'TUF', 'DUB', 'AOC', 'LHR'], 59: ['LHR', 'DUB', 'BUS', 'TUF', 'AOC', 'DUB', 'LHR'], 60: ['LHR', 'DUB', 'AOC', 'DUB', 'BUS', 'TUF', 'LHR']}
