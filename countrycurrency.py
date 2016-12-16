#countrycurrency
#version 1.0
###Author Austin Kelly
#### this module uses a supplied csv file to populate corresponding fields of a countrycurrency object###
import csv
from logerrors import *

class Countrycurrency:

    def __init__(self, country):#initialization method take country name as a string and populates attributes with key information about that countrys currency
        self.country=country
        self.getcurrency()##this method was seperated from the initialization as a learning exercise, i would incorporate the method into the init method for a production version
        ##especially as python seems to sometimes throw a 'fit' when importing the module claiming attribute doesnot exist(that cost me endless heartache) and complains intermittently if all  are not initialized in init
        self.currencycode=self.currencydetails['currency_alphabetic_code']



    def getcurrency(self):##this method reads from the supplied csv file named countrycurrency and all the info into a dictionary object with keys being the first row titles
        try:
            with open('countrycurrency.csv', encoding='utf-8', newline='') as f:##as imput is read from a file that may be missing etc i have wrap a try around it and
                # write any errors to a dynamically generated  text file called programlog so errors can be logged and worked on
                rows = csv.reader(f)
                lista = list(rows) #convert to list as python pycharm IDE complained until i did ..maybe the return object is only list like and not a list
                # print(lista)
                outerdict = {}##to be populated by for loop while processing the rows fromm file to store currency info
                keys = lista[0]
                # print(keys)
                for row in lista[1:]:  # create an object and add to outer dictionary
                    innerobj = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3], keys[4]: row[4],
                                keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8], keys[9]: row[9],
                                keys[10]: row[10], keys[11]: row[11], keys[12]: row[12], keys[13]: row[13],
                                keys[14]: row[14], keys[15]: row[15], keys[16]: row[16], keys[17]: row[17],
                                keys[18]: row[18], keys[19]: row[19]}  # add object to lib with its type as key
                    outerdict[row[0]] = innerobj#add record to lib with its key
                self.currencydetails = outerdict[self.country]###grabs only the country we have been asked for
                # print(outerdict)
                #print(outerdict['Chile'])
        except:
            Logerrors('a problem occurred in the country currency module while trying to process the countrycurrency file')

def main():##this function tests the module and should produce the results below with the assumed file
    x= Countrycurrency('Australia')
    print('Currency for ', x.country,' is ',x.currencycode,'details',x.currencydetails)


if __name__ == '__main__':
    main()
#Results  of test
#Currency for  Australia  is  AUD details {'currency_alphabetic_code': 'AUD', 'ISO3166-1-Alpha-2': 'AU', 'FIPS': 'AS', 'ISO3166-1-Alpha-3': 'AUS', 'DS': 'AUS', 'FIFA': 'AUS', 'is_independent': 'Yes', 'currency_numeric_code': '36', 'WMO': 'AU', 'IOC': 'AUS', 'ISO3166-1-numeric': '36', 'MARC': 'at', 'ITU': 'AUS', 'currency_minor_unit': '2', 'GAUL': '17', 'currency_country_name': 'AUSTRALIA', 'name_fr': 'Australie', 'name': 'Australia', 'Dial': '61', 'currency_name': 'Australian Dollar'}

