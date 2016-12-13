#airport.py
##version 1.0
###Author Austin Kelly
####This module creates airport objects using the details form the csv file read in the getdetails method. It also endows  airport objects with properties regarding the local currency
import csv
from currencyrate import *
from countrycurrency import *

class Airport:

    def getdetails(self):
        keys=['airportid','airportname','cityname','country','code','icaocode','latitude','longitude','altitude','timeoffset','dst','tz']
        with open('airports.csv', encoding='utf-8') as f:
            rows = csv.reader(f)
            lista = list(rows)
            # print(keys)
            for row in lista[:]:  # cycle throw airports and locate airport details
                airportobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
                            keys[4]: row[4],keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8],
                            keys[9]: row[9],keys[10]: row[10], keys[11]: row[11]}  # add object to lib with its model as key
                if airportobject['code'] == self.code:
                    self.details = airportobject
                #self.details=airportobject

    def __init__(self,code):
        self.code = code
        self.getdetails()
        self.longitude = float(self.details['longitude'])
        self.latitude = float(self.details['latitude'])
        self.country = self.details['country']
        self.currency = Countrycurrency(self.details['country']).currencycode
        self.currencyeurorate= float(Currencyrate(self.currency).toeuro)
        self.getdetails()




def main():
    x = Airport('TUF')
    print(x.longitude)
    print(x.code)
    print(x.latitude)
    print(x.country)
    print(x.currency)
    print(x.currencyeurorate)
if __name__=='__main__':
    main()



