#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

class RecursiveSearch():
    def __init__(self, directory, extention="KAP", myFilter=None):
        """Searches for files ending in <extention> in <directory> and all subdirectories
           Optionally supply list of file names <myFilter> to only search for files in myFilter list
           Returns list of string paths"""
        self.extention = extention.upper()
        self.filePaths = []
        self.fileList = []
        self.myFilter = myFilter
        if not directory.endswith("/"):
            directory = directory + "/"
        if os.path.exists(directory):
            self.__listFiles(directory)
        else:
            print directory, "is not a directory."
        
    def __mywalker(self, arg, directory, files):
        if self.myFilter == None:
            for f in files:
                if f.upper().endswith(self.extention):
                    self.filePaths.append(directory+"/"+f)
                    self.fileList.append(f)
        else:
            for f in files:
                if f.upper().endswith(self.extention) and ( self.myFilter.count(f) > 0 ):
                    self.filePaths.append(directory+"/"+f)
                    self.fileList.append(f)
        
    def __listFiles(self, directory):
        os.path.walk(directory, self.__mywalker, None)
        
    def getFilePaths(self):
        return self.filePaths
    
    def getNumFiles(self):
        return len(self.filePaths)
    
    def getMegaBytes(self):
        bites = 0
        for path in self.filePaths:
            bites += os.path.getsize(path)
        if bites > 0:
            return round(bites/1048576, 2)
        else:
            return bites

if __name__== "__main__":
    directory = "C:/Users/will/charts/BSB_ROOT/MXCTEST"
    rSearch = RecursiveSearch(directory, 'kap')
    for path in rSearch.getFilePaths():
        print path
    print rSearch.getNumFiles()
    print rSearch.getMegaBytes()
