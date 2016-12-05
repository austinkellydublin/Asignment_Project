
import math
def calcdist(longitude,latitude,longitude2,latitude2):
    theta=0.000000
    gamma=0.000000
    theta2 = 0.000000
    gamma2 = 0.000000
    if latitude >=0:
        theta= deg2rads(90 - latitude)
        print(theta)
    else:
        latitude=abs(latitude)
        theta= deg2rads(90 + latitude)
        print(theta)
    gamma= deg2rads(longitude)
    print('g1 ' + str(gamma))


    if latitude2 >=0:
        theta2= deg2rads(90 - latitude2)
        print('t2' + str(theta2))
    else:
        latitude2 = abs(latitude2)
        theta2= deg2rads(90 + latitude2)
        print('t2b' + str(theta2))
    gamma2= deg2rads(longitude2)
    print('g2 ' + str(gamma2))

    dist= math.acos(math.sin(theta) * math.sin(theta2)*(math.cos(gamma-gamma2)) + (math.cos(theta)) * math.cos(theta2)) * 6371

    return dist


def deg2rads(degrees):
    rads = degrees * ( 2 * math.pi )/360
    return rads

print(calcdist(-6.270075,53.421333,151.177222,-33.946111))


