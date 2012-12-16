#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FilePathSearch import RecursiveSearch
from BsbHeader import BsbHeader
from FindZoom import getZoom

class BsbOutlines():
    def __init__(self, directory, filter=None):
        self.data = {}
        fps = RecursiveSearch(directory, 'KAP', filter)
        for map_file in fps.getFilePaths():
            self._read(map_file)
    
    def _read(self, map_file):
        header = BsbHeader(map_file)
        key = header.getbasefile()
        data = [header.getname(), header.getupdated(), header.getscale(), header.getOutline(), header.getDepthUnits(), getZoom(header.getscale(), header.getCenter()[1])]
        self.data[key] = data
        
    def printdata(self):
        for key in self.data.keys():
            print key
            for line in self.data[key]:
                print line
            print "\n"
            
    def getkeys(self):
        return self.data.keys()
            
    def getname(self, key):
        return self.data[key][0]
    
    def getupdated(self, key):
        return self.data[key][1]
    
    def getscale(self, key):
        return self.data[key][2]
    
    def getoutline(self, key):
        return self.data[key][3]
    
    def getdepthunits(self, key):
        return self.data[key][4]
    
    def getzoom(self, key):
        return self.data[key][5]
    
if __name__== "__main__":
    
    bo = BsbOutlines("C:\\Users\\Will\\Downloads\\chart-test\\")
    for each in bo.getkeys():
        print each
        print bo.getoutline(each)
        print bo.getname(each)
        print bo.getupdated(each)
        print bo.getscale(each)
        print bo.getdepthunits(each)
        print bo.getzoom(each)
        print "\n"
