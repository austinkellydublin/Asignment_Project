#airport.py
##version 1.0
###Author Austin Kelly
####This module creates airport objects using the details form the csv file read in the getdetails method.
#  It also endows  airport objects with properties regarding the local currency as a convenience property
import csv
from currencyrate import *
from countrycurrency import *
from logerrors import *

class Airport:
    def __init__(self, code):##takes in code and looks up excel sheet for airport and only loads that particular airport as this is a big file
        self.code = code
        keys=['airportid','airportname','cityname','country','code','icaocode','latitude','longitude','altitude','timeoffset','dst','tz']
        try:
            with open('airports.csv', encoding='utf-8',newline='') as f:
                rows = csv.reader(f)
                lista = list(rows)
                # print(keys)
                for row in lista[:]:  # cycle throw airports and locate airport details
                    airportobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
                                     keys[4]: row[4], keys[5]: row[5], keys[6]: row[6], keys[7]: row[7],
                                     keys[8]: row[8],
                                     keys[9]: row[9], keys[10]: row[10],
                                     keys[11]: row[11]}  # add object to lib with its model as key

                    if airportobject['code'] == self.code:
                        self.details=airportobject
                        self.longitude = float(airportobject['longitude'])
                        self.latitude = float(airportobject['latitude'])
                        self.country = airportobject['country']
                        self.currency = Countrycurrency(airportobject['country']).currencycode
                        # print(self.currency)
                        self.currencyeurorate = float(Currencyrate(self.currency).toeuro)
                        # print(self.currencyeurorate)
                        # self.currencyeurorate = float(Currencyrate(self.currency))

        except:Logerrors(' an problem with reading the airports file happened in airport module starting line 18')


def main():##this method test the mmodule it should return the results below
    x = Airport('DUB')
    print('For Dublin airport code DUB')
    print('The longitude is ',x.longitude)
    print('The code is ',x.code)
    print('The latitude is',x.latitude)
    print('The country is ',x.country)
    print('The currency is ',x.currency)
    print('The to euro rate for fuel is ',x.currencyeurorate)
if __name__=='__main__':
    main()
##RESULTS OF TEST SHOULD BE AS PER BELOW
# For Dublin airport code DUB
# The longitude is  -6.270075
# The code is  DUB
# The latitude is 53.421333
# The country is  Ireland
# The currency is  EUR
# The to euro rate for fuel is  1.0



