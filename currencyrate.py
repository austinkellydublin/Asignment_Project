import csv

class Currencyrate:
    def __init__(self,currencycode):
        self.currencycode=currencycode
        self.getcurrencyrate()
        self.toeuro = self.currencyratedetails['toeuro']
        self.fromeuro = self.currencyratedetails['fromeuro']

    def getcurrencyrate(self):
        with open('currencyrates.csv', encoding='utf-8', newline='') as f:
            outerdict = {}
            keys = ['currencyname', 'currencycode', 'toeuro', 'fromeuro']
            rows = csv.reader(f)
            lista = list(rows)
            print(keys)
            for row in lista[:]:  # create an object
                innerobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2],
                               keys[3]: row[3]}  # add object to lib with its model as key
                outerdict[row[1]] = innerobject  # add record retrievable by currency code
            self.currencyratedetails = outerdict[self.currencycode]
                # print(outerdict['ARS'])
                # print(outerdict['AUD'])
def main():
    x= Currencyrate('AUD')


    print(x.toeuro)
    print(x.fromeuro)

main()
