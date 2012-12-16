#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

import codecs
import BsbOutlines
import time
import os.path
import zipfile

str0 = "UPDATE regions SET installeddate='%s' WHERE name='%s';\n"
strcustom0 = u"DELETE from regions WHERE name='%s';\n"
strcustom1 = u"INSERT into [regions] ([name], [description], [image], [size], [installeddate] ) VALUES ('%s', '%s', '%s', '%s', '%s');\n"
str1 = u"DELETE from charts where region='%s';\n"
str2 = u"INSERT INTO [charts] ([region], [file], [name], [updated], [scale], [outline], [depths], [zoom]) VALUES ('%s', '%s', '%s', '%s', %s, '%s', '%s', '%s');\n"
custom = True;
epoch = int(time.time())

def generateRegion(name, desc, indir, outdir, myFilter = None):
    #fisrt lets see if the gemf is there
    
    print "generating data for " + name
    bo = BsbOutlines.BsbOutlines(indir, myFilter)
    sqlFname = name+".sql"
    sqlPath = outdir+"/"+sqlFname
    zdatPath = outdir+"/"+name+".zdat"
    sqlf = codecs.open(sqlPath, "w", "utf-8")
    zdat = zipfile.ZipFile(zdatPath, "w", zipfile.ZIP_DEFLATED)
    #sqlf = open(Env.gemfDir+"/"+region+".bin", "wb")
    
    wrt = u"--MXMARINER-DBVERSION:3\n"
    #zdat.writestr( sqlFname, wrt)
    sqlf.write( wrt )
    
    if (custom):
        gemfFile = outdir + "/" + name + ".gemf"
        wrt = strcustom0 %(name)
        sqlf.write( wrt )
        
        wrt = strcustom1 %(name, desc, name.lower().replace("_", ""), os.path.getsize(gemfFile), epoch)
        sqlf.write( wrt )
    else:
        wrt = str0 %(epoch, name)
        sqlf.write( wrt )
    
    wrt = str1 %(name) 
    sqlf.write( wrt )
    
    for kapfile in bo.getkeys():
        wrt = str2 %(name, kapfile, bo.getname(kapfile), bo.getupdated(kapfile), bo.getscale(kapfile), \
                     bo.getoutline(kapfile), bo.getdepthunits(kapfile), bo.getzoom(kapfile));
        sqlf.write( wrt )
    
    sqlf.close()
    zdat.write(sqlPath, sqlFname)
    os.remove(sqlPath)
    zdat.close()
    print "data generation complete"
    
