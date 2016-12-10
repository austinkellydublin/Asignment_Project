# import csv


# # with open('aircraft.csv') as f:
# #     rows = csv.reader(f)
# #     lista=list(rows)
# #     print(lista)
# #     outerdict={}
# #     keys=lista[0]
# #     print(keys)
# #     for row in lista[1:]:#create an object and add to outer dictionary
# #         innerobj={keys[0]:row[0],keys[1]:row[1],keys[2]:row[2],keys[3]:row[3],keys[4]:row[4]}#add object to lib with its type as key
# #         outerdict[row[0]]=innerobj
# #     print(outerdict)
# #     print(outerdict['777'])
# #     print(outerdict['747'])
#
# # with open('countrycurrency.csv',encoding='utf-8',newline='') as f:
# #     rows = csv.reader(f)
# #     lista=list(rows)
# #    # print(lista)
# #     outerdict={}
# #     keys=lista[0]
# #    # print(keys)
# #     for row in lista[1:]:#create an object and add to outer dictionary
# #         innerobj={keys[0]:row[0],keys[1]:row[1],keys[2]:row[2],keys[3]:row[3],keys[4]:row[4],keys[5]:row[5],keys[6]:row[6],keys[7]:row[7],keys[8]:row[8],keys[9]:row[9],keys[10]:row[10],keys[11]:row[11],keys[12]:row[12],keys[13]:row[13],keys[14]:row[14],keys[15]:row[15],keys[16]:row[16],keys[17]:row[17],keys[18]:row[18],keys[19]:row[19]}#add object to lib with its type as key
# #         outerdict[row[0]]=innerobj
# #     #print(outerdict)
# #     print(outerdict['Ireland'])
# #     print(outerdict[])
#
# # with open('currencyrates.csv', encoding='utf-8', newline='') as f:
# #     outerdict = {}
# #     keys=['currencyname','currencycode','toeuro','fromeuro']
# #     rows = csv.reader(f)
# #     lista = list(rows)
# #     print(keys)
# #     for row in lista[:]:  # create an object
# #         innerobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3]}  # add object to lib with its model as key
# #         outerdict[row[1]]=innerobject #add record retrievable by currency code
#     # print(outerdict['ARS'])
#     # print(outerdict['AUD'])
# ##airport.py
# # import csv
# #
# #
# # class Airport:
# #
# #     def getdetails(self):
# #         keys=['airportid','airportname','cityname','country','code','icaocode','latitude','longitude','altitude','timeoffset','dst','tz']
# #         with open('airports.csv', encoding='utf-8') as f:
# #             rows = csv.reader(f)
# #             lista = list(rows)
# #             # print(keys)
# #             for row in lista[:]:  # create an object
# #                 airportobject = {keys[0]: row[0], keys[1]: row[1], keys[2]: row[2], keys[3]: row[3],
# #                             keys[4]: row[4],keys[5]: row[5], keys[6]: row[6], keys[7]: row[7], keys[8]: row[8],
# #                             keys[9]: row[9],keys[10]: row[10], keys[11]: row[11]}  # add object to lib with its model as key
# #                 if airportobject['code'] == self.code:
# #                     self.details = airportobject
# #
# #     def __init__(self,code):
# #         self.code = code
# #         self.getdetails()
# #         self.longitude = float(self.details['longitude'])
# #         self.latitude = float(self.details['latitude'])
# #         self.country = self.details['country']
# #
# #
# #
# # def main():
# #     x = Airport('DUB')
# #     print(x.longitude)
# #     print(x.code)
# #     print(x.latitude)
# #     print(x.country)
# #
# # if __name__=='__main__':
# #     main()
#
# # candidateroutes= list(permutations(['YYG','LHR','YYJ','DUB','YYN','YYH']))
# # print(candidateroutes)
# # print(len(candidateroutes))
# # for i in candidatesroutes:
#
# leglist=[23,56,13,56,15,66,13,13,33,18]
# # print(len(leglist))
# # priceofleg=[1.23,2.3,1.3,1.23,1.1,1.5,1.3,2.0,1.3,1.5]
# # print(len(priceofleg))
# # fuelrange=0
# # range=90
# # cheapestinrange=''
# # rangeee=o
# # for index,value in (enumerate(leglist)):
# #     print(index,value)
# #     while rangee <= range:
#
#
# self.portlist_inrange = {}
# rangedict = {}
# for i in range(1: 7):  # loop for each airport
#     for k in range(i: 7):  # only consider legs beyond airport to build dictionary of lists for reach port from a given airport
#         rangelist = []
#         strikerange = 0
#          portlist_inrange[i] = {}
#          if strikerange + leglist[ k] < range:  # if haven't gone beyond range examine next leg as candidate for reachables
#             strikerange += leglist[k]  # increment distance travelled
#             rangelist.append(portlist[k + 1])  # append end port to reachable list
#             portlist_inrange[i] = rangelist  # update list of reachable ports for a given airport
#
#
#




def portsinrange(self):
    todelete = []
    ##to implement fuelling strategy for each candidate route  examine legs to determine which distant ports would be with in reach for each port
    ##so at each airport will need a list of airports within fuel tank range these will be stored in a dictionary portlist_inrange
    maxfuelrange = self.craft.range  ## get fuel tank range
    leginfo = {}  # this dictionary will shadow candidate dictionary and store a reach stations ahead for each point on route
    for candkey, cand in self.candidates.items():  # get each candidate route
        cand = list(cand)  # a candidate route is a list of ordered ports
        # candidates get processed differently depending if have five or six legs
        # print('here we go',index,'  ',portlista)
        if candkey < 24:  # for five legged journeys
            legslist = Legdistances(cand[0], cand[1], cand[2], cand[3], cand[4], cand[5]).legslist
            legslist.pop()
            for leg in legslist:
                if leg > maxfuelrange:
                    todelete.append(candkey)
                    #### TODO NEED TO STORE TO DELETE EARLIER IF LEGS ARE GREATER THAN RANGE
            print(candkey, '  ', legslist)
            for i in range(0, 5):  # for  all ports up to last port but excluding it
                # print('i', i)
                leginfo[i] = []  # setup parent list for children lists
                inrangelist = []  # set up child list
                fuel = maxfuelrange
                for k in range(i, 5):  # for sucessive ports there are less ports ahead
                    # print('k', k)
                    if fuel >= legslist[k]:  #
                        inrangelist.append(cand[k + 1])  # add port at end of leg as reachable
                        leginfo[i] = inrangelist  # update parent list with amended child
                        fuel -= legslist[
                            k]  # adjust fuel in algorithm else will evaluate other legs and include them if the pass criteria
                    else:
                        break  # if any port out of range then no sense in evaluating more distant ports so set fuel to zero

                        # update list of reachable ports for a given airport
            self.candidates[candkey].append(leginfo)
            # print(candkey,'   ',self.candidates)
            # print(candkey, '\n'', self.candidates[candkey])
        if candkey >= 24:  ##then will have 7 airports and 6 legs
            legslist = Legdistances(cand[0], cand[1], cand[2], cand[3], cand[4], cand[5], cand[6]).legslist
            # print(candkey,'  ',legslist)
            for i in range(0, 6):  # for  all ports up to last port
                # print('i', i)
                leginfo[i] = []
                inrangelist = []
                fuel = maxfuelrange
                for k in range(i, 6):  # for legs ahead each port
                    # print('k', k)
                    if fuel >= legslist[k]:
                        inrangelist.append(cand[k + 1])
                        leginfo[i] = inrangelist
                        fuel -= legslist[
                            k]  # even route out of range must adjust fuel in algorithm else will evaluate other legs and include them if the pass criteria
                    else:
                        break
            self.candidates[candkey].append(leginfo)
            flaga = False
            for eacha, listg in self.candidates[candkey][-1].items():
                if len(list(listg)) == 0:
                    flaga = True
            if flaga == True:
                todelete.append(candkey)
                # print(candkey, '   ', self.candidates)

    for each in todelete:
        del self.candidates[each]

    print(self.candidates)
    #     self.candidates[candkey].append(leginfo)
    #     # dicta = self.candidates[candkey][-1]
    #     # for eacha, listg in dicta.items():
    #     #     if len(listg) == 0:
    #     #         del self.candidates[candkey]
    #     print(self.candidates[candkey])
    # self.candidates[candkey].append(leginfo)
    # print(candkey, '\n\n', cand, '\n', leginfo, '\n\n')
    # dicta=self.candidates[-1]
    # print(dicta[0],'  ',dicta[4])












