#importdata.py
##version 1.0
###Author Austin Kelly
####this module imports user csv file and passes data to the best route function for processing
from route import *
from csv import *

class Importdata():
    def __init__(self,filename):
        filename=str(filename).strip()
        pass
        # if not (filename.endswith('.csv') or (filename.endswith('.xls')):
        #     ###TODO raise an error
        #     pass
        # else:row[0],row[1],row[2],row[3],row[4],row[5]
        with open(filename,encoding='UTF-8',newline='') as f:
            rows = csv.reader(f)
            lista=list(rows)
            print(lista)
            masterlist=[]
            for row in lista:
                routedata=[row[0],row[1],row[2],row[3],row[4],row[5]]
                bestroute= Route(row[0],row[1],row[2],row[3],row[4],row[5]).cheapest_route
                print(bestroute)
                masterlist.append(bestroute)###now have an array of list each which is the best route
            for bestroute in masterlist:
                with open('result_for_file_'+filename,'w',encoding='utf-8',newline='') as f:
                    writer=csv.writer(f)
                    for row in masterlist:
                        writer.writerow(row)
x= Importdata('test21.csv')

# masterlist = [['row1','row1','row11','row1','row1','row1']]
# best = ['row12','row1','row1','row1','row1','row1']
# masterlist.append(best)
# for best in masterlist:
#     with open('result_for_' + '.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         for itema in masterlist:
#             writer.writerow(itema)








        #
        #         pass
        #
        # def getcurrencyrate(self):
        #     with open('currencyrates.csv', encoding='utf-8',
        #               newline='') as f:  # opens a csv file and returns a 'fileobject' referenced below as f
        #         outerdict = {}  # a dictionary to be populated with a collection of dictionary objects, one for each currency and accessed by the currencycode as key with internal details keyed by column namess
        #         keys = ['currencyname', 'currencycode', 'toeuro', 'fromeuro']  # keys of internal dictionarys
        #         rows = csv.reader(f)  # returns a tuple
        #         lista = list(rows)  # convert to a list proper
        #         # uncomment below to test keys
        #         # print(keys)
        #         for row in lista[:]:  # create an object
        #             innerobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2],
        #                            keys[3]: row[3]}  # add object to lib with its model as key
        #             outerdict[row[1]] = innerobject  # add record retrievable by currency code
        #         self.currencyratedetails = outerdict[
        #             self.currencycode]
        #






