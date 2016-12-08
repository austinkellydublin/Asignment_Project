from route import *






def portsinrange(self):
    ranger = 5000

    self.portlist_inrange = {}
    # rangedict={}
    for i in range(0, 6):
        # print(i)
        self.portlist_inrange[i] = []
        rangelist = []
        strikerange = 0
        for k in range(i,
                       6):  # only consider legs beyond airport to build dictionary of lists for reach port from a given airport
            if (strikerange + self.legslist[
                k]) < ranger:  # if haven't gone beyond range examine next leg as candidate for reachables
                strikerange += self.legslist[k]  # increment distance would have travelled
                rangelist.append(self.portlist[k + 1].code)  # append end port to reachable list
                self.portlist_inrange[i] = rangelist  # update list of reachable ports for a given airport
                # print(self.portlist_inrange)
            else:
                break
    print(self.portlist_inrange)
    # print([self.port1.code, self.port2.code, self.port3.code, self.port4.code, self.port5.code, self.port6.code, self.port7.code])
    # print(self.portlist[3].code)
