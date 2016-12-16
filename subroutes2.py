from legdistances import *

class Subroutes():
    def __init__(self,route,tank_range):
       # print('tank =',tank_range)
        #print('route',route)

        if len(route)<7:
            #print('entered first loop')
            #list of leg distances
            legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5]).legslist
            legsdist.pop()
            #print(legsdist)
            #print('legdists',legsdist)
            ## the holding array that stores all the subroute lists

            masterlist=[]# from each port can fuel up so want to see how many ports can reach on full tank
            for port in range(5): ##at each of the 6 ports
                # print('start fuel',fuel)
                fuel = tank_range##can refil
                aports_subroute = []## see who can reach
                for leg in range(port, 6):#for each leg from a port
                    if (legsdist[leg]) > fuel :
                        # if next port(legdistance) impossible to reach append subroute and stop building for this port
                        break  # stop building the chain when a leg to far is reached
                    else:

                        #print(route[leg+1])
                        aports_subroute.append(route[leg+1])
                       # print(legsdist[leg])# keeping building chain
                        fuel -= legsdist[leg]
                       # print(fuel)

                        if leg == 4:
                            #print('hell3')
                            break
                        # if leg == 4:  ##only a five leg journey so done last leg append and break
                        #     break  ##donot need this break but good to highlight logic
                masterlist.append(aports_subroute)
                self.subroutes=masterlist
        if len(route) >=7:
            # print('entered first loop')
            # list of leg distances
            legsdist = Legdistances(route[0], route[1], route[2], route[3], route[4], route[5],route[6]).legslist

            # print(legsdist)
            # print('legdists',legsdist)
            ## the holding array that stores all the subroute lists

            masterlist = []  # from each port can fuel up so want to see how many ports can reach on full tank
            for port in range(6):  ##at each of the 6 ports
                # print('start fuel',fuel)
                fuel = tank_range  ##can refil
                aports_subroute = []  ## see who can reach
                for leg in range(port, 7):  # for each leg from a port
                    if (legsdist[leg]) > fuel:
                        # if next port(legdistance) impossible to reach append subroute and stop building for this port
                        break  # stop building the chain when a leg to far is reached
                    else:

                        # print(route[leg+1])
                        aports_subroute.append(route[leg + 1])
                        # print(legsdist[leg])# keeping building chain
                        fuel -= legsdist[leg]
                        # print(fuel)

                        if leg == 5:
                            # print('hell3')
                            break
                            # if leg == 4:  ##only a five leg journey so done last leg append and break
                            #     break  ##donot need this break but good to highlight logic
                masterlist.append(aports_subroute)
                self.subroutes = masterlist








def main():
    x=Subroutes(['LHR', 'TUF', 'AOC', 'BHX','DUB', 'LHR'],7000)
    y=['LHR', 'TUF', 'AOC', 'BHX', 'BUS', 'DUB', 'LHR']
    print('original route',y)
    print('subroutes reachable on each leg within full tank range are ',x.subroutes)
if __name__ == '__main__':
    main()

