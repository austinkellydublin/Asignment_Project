#calculatedistance
import math

class Calcdistance:
    def __init__(self,longitude1,latitude1,longitude2,latitude2):
        self.longitude = longitude1
        self.latitude = latitude1
        self.longitude2 = longitude2
        self.latitude2 = latitude2
        self.distance = self.calcdist()


    def calcdist(self):
        theta = 0.000000
        gamma = 0.000000
        theta2 = 0.000000
        gamma2 = 0.000000
        if self.latitude >= 0:
            theta = self.deg2rads(90 - self.latitude)
            # print(theta)
        else:
            theta = self.deg2rads(90 + abs(self.latitude))
            # print(theta)
        gamma = self.deg2rads(self.longitude)
        # print('g1 ' + str(gamma))


        if self.latitude2 >= 0:
            theta2 = self.deg2rads(90 - self.latitude2)
            #  print('t2' + str(theta2))
        else:

            theta2 = self.deg2rads(90 + abs(self.latitude2))
            # print('t2b ' + str(theta2))
        gamma2 = self.deg2rads(self.longitude2)
        # print('g2 ' + str(gamma2))

        dist = math.acos(math.sin(theta) * math.sin(theta2) * (math.cos(gamma - gamma2)) + (math.cos(theta)) * math.cos(
            theta2)) * 6371

        return dist

    def deg2rads(self, degrees):
        rads = degrees * (2 * math.pi) / 360
        return rads

        #  print(calcdist(-6.270075,53.421333,151.177222,-33.946111))


