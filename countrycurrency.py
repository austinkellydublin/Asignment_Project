#countrycurrency
#version 1.0
###Author Austin Kelly
#### this module uses a magic named csv file to populate corresponding fields of a countrycurrency object
import csv

class Countrycurrency:

    def __init__(self, country):
        self.country=country
        self.getcurrency()
        self.currencycode=self.currencydetails['currency_alphabetic_code']



    def getcurrency(self):
        with open('countrycurrency.csv', encoding='utf-8', newline='') as f:
            rows = csv.reader(f)
            lista = list(rows)
            # print(lista)
            outerdict = {}
            keys = lista[0]
            # print(keys)
            for row in lista[1:]:  # create an object and add to outer dictionary
                innerobj = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3], keys[4]: row[4],
                            keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8], keys[9]: row[9],
                            keys[10]: row[10], keys[11]: row[11], keys[12]: row[12], keys[13]: row[13],
                            keys[14]: row[14], keys[15]: row[15], keys[16]: row[16], keys[17]: row[17],
                            keys[18]: row[18], keys[19]: row[19]}  # add object to lib with its type as key
                outerdict[row[0]] = innerobj#add record to lib with its key
            self.currencydetails = outerdict[self.country]
            # print(outerdict)
            #print(outerdict['Chile'])

def main():
    x= Countrycurrency('Australia')
    print(x.currencycode)

if __name__ == '__main__':
    main()

