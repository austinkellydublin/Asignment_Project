#importdata.py
##version 1.0
###Author Austin Kelly
'''   module imports user csv file and passes data to the best route function for processing, it then gets back the result as a list and stores it in a masterlist
and then writes the data to a csv file named the same as the original file but with a   result_for_file_   prefix
'''
from route import *
from csv import *
from logerrors import *

class Importdata():
    def __init__(self,filename):
        filename=str(filename).strip()##strip of white space either side of file name
        try:
            with open(filename,encoding='UTF-8',newline='') as f:###read in file and pull out routes
                rows = csv.reader(f)
                lista=list(rows)
                #print(lista)
                masterlist=[]
                for row in lista:
                    routedata=[row[0],row[1],row[2],row[3],row[4],row[5]]
                    bestroute= Route(row[0],row[1],row[2],row[3],row[4],row[5]).cheapest_route### create route object with data from csv file and call its cheapest route method
                    #print(bestroute)
                    masterlist.append(bestroute)###now have an array of list each which is the best route
                for bestroute in masterlist:
                    with open('result_for_file_'+filename,'w',encoding='utf-8',newline='') as f: ##open/create file with same name as orginal but prefixed results for file
                        writer=csv.writer(f)
                        for row in masterlist:
                            writer.writerow(row)
        except:Logerrors('a problem occured in the importdata module during processing a route csv file')
       # print('all went ok')



def main():
    x = Importdata('test2.csv')
if __name__ == '__main__':
    main()
# masterlist = [['row1','row1','row11','row1','row1','row1']]
# best = ['row12','row1','row1','row1','row1','row1']
# masterlist.append(best)
# for best in masterlist:
#     with open('result_for_' + '.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.writer(f)
#         for itema in masterlist:
#             writer.writerow(itema)


