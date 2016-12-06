# import csv
from itertools import *
from route import *

# with open('aircraft.csv') as f:
#     rows = csv.reader(f)
#     lista=list(rows)
#     print(lista)
#     outerdict={}
#     keys=lista[0]
#     print(keys)
#     for row in lista[1:]:#create an object and add to outer dictionary
#         innerobj={keys[0]:row[0],keys[1]:row[1],keys[2]:row[2],keys[3]:row[3],keys[4]:row[4]}#add object to lib with its type as key
#         outerdict[row[0]]=innerobj
#     print(outerdict)
#     print(outerdict['777'])
#     print(outerdict['747'])

# with open('countrycurrency.csv',encoding='utf-8',newline='') as f:
#     rows = csv.reader(f)
#     lista=list(rows)
#    # print(lista)
#     outerdict={}
#     keys=lista[0]
#    # print(keys)
#     for row in lista[1:]:#create an object and add to outer dictionary
#         innerobj={keys[0]:row[0],keys[1]:row[1],keys[2]:row[2],keys[3]:row[3],keys[4]:row[4],keys[5]:row[5],keys[6]:row[6],keys[7]:row[7],keys[8]:row[8],keys[9]:row[9],keys[10]:row[10],keys[11]:row[11],keys[12]:row[12],keys[13]:row[13],keys[14]:row[14],keys[15]:row[15],keys[16]:row[16],keys[17]:row[17],keys[18]:row[18],keys[19]:row[19]}#add object to lib with its type as key
#         outerdict[row[0]]=innerobj
#     #print(outerdict)
#     print(outerdict['Ireland'])
#     print(outerdict[])

# with open('currencyrates.csv', encoding='utf-8', newline='') as f:
#     outerdict = {}
#     keys=['currencyname','currencycode','toeuro','fromeuro']
#     rows = csv.reader(f)
#     lista = list(rows)
#     print(keys)
#     for row in lista[:]:  # create an object
#         innerobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3]}  # add object to lib with its model as key
#         outerdict[row[1]]=innerobject #add record retrievable by currency code
    # print(outerdict['ARS'])
    # print(outerdict['AUD'])
##airport.py
# import csv
#
#
# class Airport:
#
#     def getdetails(self):
#         keys=['airportid','airportname','cityname','country','code','icaocode','latitude','longitude','altitude','timeoffset','dst','tz']
#         with open('airports.csv', encoding='utf-8') as f:
#             rows = csv.reader(f)
#             lista = list(rows)
#             # print(keys)
#             for row in lista[:]:  # create an object
#                 airportobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
#                             keys[4]: row[4],keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8],
#                             keys[9]: row[9],keys[10]: row[10], keys[11]: row[11]}  # add object to lib with its model as key
#                 if airportobject['code'] == self.code:
#                     self.details = airportobject
#
#     def __init__(self,code):
#         self.code = code
#         self.getdetails()
#         self.longitude = float(self.details['longitude'])
#         self.latitude = float(self.details['latitude'])
#         self.country = self.details['country']
#
#
#
# def main():
#     x = Airport('DUB')
#     print(x.longitude)
#     print(x.code)
#     print(x.latitude)
#     print(x.country)
#
# if __name__=='__main__':
#     main()

# candidateroutes= list(permutations(['YYG','LHR','YYJ','DUB','YYN','YYH']))
# print(candidateroutes)
# print(len(candidateroutes))
# for i in candidatesroutes:

leglist=[23,56,13,56,15,66,13,13,33,18]
print(len(leglist))
priceofleg=[1.23,2.3,1.3,1.23,1.1,1.5,1.3,2.0,1.3,1.5]
print(len(priceofleg))
fuelrange=0
range=90
cheapestinrange=''
rangeee=o
for index,value in (enumerate(leglist)):
    print(index,value)
    while rangee <= range:























