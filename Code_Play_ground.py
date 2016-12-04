import csv

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

keys=['airportid','airportname','cityname','country','code','icaocode','latitude','longitude','altitude','timeoffset','dst','tz']
print(keys)
with open('airports.csv',encoding='utf-8') as f:
    rows = csv.reader(f)
    lista = list(rows)

    for row in lista[:]:  # create an object
        airportobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
                         keys[4]: row[4], keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8],
                         keys[9]: row[9], keys[10]: row[10], keys[11]: row[11]}  # add object to lib with its model as key
        if airportobject['code'] == 'DUB':
            print(airportobject)
















