#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import codecs, BsbOutlines, time, os.path

#        CREATE TABLE regions ( 
#            name          TEXT,
#            description   TEXT,
#            image         TEXT,
#            size          INT,
#            installeddate INT,
#            latestdate    INT );

str0 = "UPDATE regions SET installeddate='%s' WHERE name='%s';\n"
strcustom0 = u"DELETE from regions WHERE name='%s';\n"
strcustom1 = u"INSERT into [regions] ([name], [description], [image], [size], [installeddate] ) VALUES ('%s', '%s', '%s', '%s', '%s');\n"
str1 = u"DELETE from charts where region='%s';\n"
str2 = u"INSERT INTO [charts] ([region], [file], [name], [updated], [scale], [outline], [depths]) VALUES ('%s', '%s', '%s', '%s', %s, '%s', '%s');\n"
#dir = '/home/will/charts/gemfs_version2'
#region = "REGION_40"
#epoch = "1324500235"
#epoch = "1331534724"
custom = True;
epoch = int(time.time())
        
def generateRegion(name, desc, indir, outdir, myFilter = None):
    #fisrt lets see if the gemf is there
    
    print "generating data for region: " + name
    bo = BsbOutlines.BsbOutlines(indir, myFilter)
    sqlf = codecs.open(outdir+"/"+name+".data", "w", "utf-8")
    
    wrt = u"mx.mariner.data\n"
    sqlf.write( wrt )
    
    if (custom):
        gemfFile = outdir + "/" + name + ".gemf"
        bytes = os.path.getsize(gemfFile)
        wrt = strcustom0 %(name)
        sqlf.write( wrt )
        
        #[name], [description], [image], [size], [installeddate]
        wrt = strcustom1 %(name, desc, name.lower().replace("_", ""), bytes, epoch)
        sqlf.write( wrt )
    else:
        wrt = str0 %(epoch, name)
        sqlf.write( wrt )
    
    wrt = str1 %(name) 
    sqlf.write( wrt )
    
    for kapfile in bo.getkeys():
        wrt = str2 %(name, kapfile, bo.getname(kapfile), bo.getupdated(kapfile), bo.getscale(kapfile), bo.getoutline(kapfile), bo.getdepthunits(kapfile))
        sqlf.write( wrt )
    
    sqlf.close()
    print "data generation complete"
