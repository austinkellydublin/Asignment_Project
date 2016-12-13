#currencyrate
#version 1.0
###Author Austin Kelly
##This module is to create currency rate objects when given a currency code
import csv

class Currencyrate:
    #currencyrate it the main class and will
    def __init__(self,currencycode):
        self.currencycode=currencycode
        self.getcurrencyrate()#call internal getcurrency method to populate toeuro and fromeuro fields
        self.toeuro = self.currencyratedetails['toeuro']#stores the toeuro rate
        self.fromeuro = self.currencyratedetails['fromeuro']#stores the from euro rate

    def getcurrencyrate(self):
        #this method is used by the initializer to dynamically fetch the currency rates from
        with open('currencyrates.csv', encoding='utf-8', newline='') as f:#opens a csv file and returns a 'fileobject' referenced below as f
            outerdict = {} # a dictionary to be populated with a collection of dictionary objects, one for each currency and accessed by the currencycode as key with internal details keyed by column namess
            keys = ['currencyname', 'currencycode', 'toeuro', 'fromeuro']#keys of internal dictionarys
            rows = csv.reader(f)#returns a tuple
            lista = list(rows)#convert to a list proper
           #uncomment below to test keys
            #print(keys)
            for row in lista[:]:  # create an object
                innerobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2],
                               keys[3]: row[3]}  # add object to lib with its model as key
                outerdict[row[1]] = innerobject  # add record retrievable by currency code
            self.currencyratedetails = outerdict[self.currencycode] #can access all the info but we only require some of it at this stage
            # uncomment below to test
            #print(outerdict['ARS'])
            #print(outerdict['AUD'])
def main():
    ##this contains test code if module run as a standalone script
    x= Currencyrate('AUD')
    print(x.toeuro)
    print(x.fromeuro)

if __name__=='__main__':
    main()
