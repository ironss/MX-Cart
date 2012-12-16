#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Copyright (C) 2010 by Will Kamp <manimaul!gmail.com>

#C:\path\to\src>python buildWin.py build

from cx_Freeze import setup, Executable
import sys, os, shutil, Resources

if sys.platform == 'win32':
    base = "Console" #Console or Win32GUI

packages = ["sys", "os", "glob", "gdal", "logging", "shutil", "subprocess", "itertools", "re", "shutil", "locale", "json", "shapely.geometry", "math", "operator", "struct", "pyproj"]
path = sys.path
path.append("C:\\Users\\will\\workspace-python\\MXCart\\my_tilers_tools")

bits = 32

def getOutputDir():
    if bits == 32:
        return "exe.win32-2.7"
    if bits == 64:
        return "exe.win-amd64-2.7"
 
def getPyprojDataDir():
    if bits == 32:
        return "C:/Python27/Lib/site-packages/pyproj/data/"
    if bits == 64:
        return "C:/Python27/Lib/site-packages/pyproj/data/"

directory = '%s/build/%s/data' %(os.path.dirname(__file__), getOutputDir())
directory = directory.replace("\\", "/")
print "********************************"
print directory
if not os.path.isdir(directory):
    print "********************************"
    os.makedirs(directory)

for each in os.listdir(getPyprojDataDir()):
    shutil.copy2(getPyprojDataDir() + each, directory)
    #zipincludes.append( (getPyprojDataDir() + each, "pyproj/data/" + each))
    
build_exe_options = {"packages": packages, "compressed": True, "path": path, "base": base }
 
setup(  name='MXCart', 
        version  = Resources.versionNum,
        description = 'MX Mariner Chart Data Converter',
        options = {"build_exe": build_exe_options},
        executables = [Executable("MXCart.py", base=base, targetName="MXCart.exe", copyDependentFiles=True, icon='icon.ico')]
      )

if bits == 64:
    shutil.copy2('C:/Python27/Lib/site-packages/shapely/geos_c.dll', 'build/%s' %(getOutputDir()) )
if bits == 32:
    shutil.copy2('C:/Python27/Lib/site-packages/shapely/geos_c.dll', 'build/%s' %(getOutputDir()) )
    #shutil.copy2('C:/Python27/DLLs/geos.dll', 'build/%s' %(getOutputDir()) )


shutil.copy2('MUI_WELCOMEFINISHPAGE_BITMAP.bmp', 'build/%s' %(getOutputDir()) ) 
shutil.copy2('MUI_HEADERIMAGE_BITMAP.bmp', 'build/%s' %(getOutputDir()) ) 
shutil.copy2('license.txt', 'build/%s' %(getOutputDir()) ) 
shutil.copy2('icon.ico', 'build/%s' %(getOutputDir()) ) 
shutil.copy2('pngnqi.exe', 'build/%s' %(getOutputDir()) ) 
shutil.copy2('spinner.gif', 'build/%s' %(getOutputDir()) )    
shutil.copy2('kattegat.png', 'build/%s' %(getOutputDir()) )
shutil.copy2('reader_bsb_data.csv', 'build/%s' %(getOutputDir()) )
shutil.copy2('viewer-google.html', 'build/%s' %(getOutputDir()) )
shutil.copy2('viewer-openlayers.html', 'build/%s' %(getOutputDir()) )