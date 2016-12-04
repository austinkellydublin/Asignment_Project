##aircraft.py
import csv

class Aircraft:


    def __init__(self, model):
        self.model=model
        self.object_details()

    def object_details(self):
        with open('aircraft.csv') as f:
            rows = csv.reader(f)
            lista = list(rows)
           # print(lista)
            outerdict = {}
            keys = lista[0]
           # print(keys)
            for row in lista[1:]:  # create an object and add to outer dictionary
                innerobj = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
                            keys[4]: row[4]}  # add object to lib with its model as key
                outerdict[row[0]] = innerobj
            #print(outerdict)
           # print(outerdict['777']) #returns details record for 777 plane

        self.details = outerdict[self.model]
        self.range = int(self.details['range'])






def main():
    x = Aircraft('777')
    print(x.details)
    print(x.range)
if __name__ == '__main__' :
    main()

























