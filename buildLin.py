import os, hashlib
from shutil import copy2 as copy
from Resources import versionNum
from subprocess import Popen
from shutil import rmtree

def md5sum(fd, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = fd.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

#clean any previous
mPath = os.path.dirname(__file__)+"/build/debpkg/"
if os.path.isdir(mPath):
    rmtree(mPath)

#create DEBIAN directory
mPath = os.path.dirname(__file__)+"/build/debpkg/DEBIAN"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
    
#write control file
control = open(mPath+"/control", "w")
control.write( "Package: MXCart\n" + \
    "Version: %s\n" %(versionNum) + \
    "Section: misc\n" + \
    "Priority: optional\n" + \
    "Architecture: all\n" + \
    "Depends: pngnq, python, python-wxgtk2.8, python-imaging, python-gdal, python-pyproj, python-simplejson, python-shapely\n" + \
    "Installed-Size: 331\n" + \
    "Maintainer: Will Kamp\n" + \
    "Description: BSB version 2 and 3 chart import utility for MX Mariner\n" )
control.close()

#copy over needed python files
mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/lib/mxcart/"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
for pyFile in ["/BsbHeader.py", "/buildWin.py", "/GUI.py", "/MXCart.py", "/BsbScales.py", \
               "/BsbOutlines.py", "/FilePathSearch.py", "/Helper_Gdal.py", "/MyGemfBuilder.py", \
               "/Helper_Tiler.py", "/Helper_Merge.py", "/Resources.py", "/FindZoom.py", "/GenerateData.py", \
               "/reader_bsb_data.csv", "/my_tilers_tools/viewer-google.html", "/my_tilers_tools/viewer-openlayers.html"]:
    #print os.path.dirname(__file__)+pyFile, mPath
    copy(os.path.dirname(__file__)+pyFile, mPath)
    
mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/lib/mxcart/my_tilers_tools/"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
for pyFile in ["/my_tilers_tools/gdal_tiler.py", \
               "/my_tilers_tools/generate_efficient_map_file.py", \
               "/my_tilers_tools/map2gdal.py", \
               "/my_tilers_tools/reader_backend.py", \
               "/my_tilers_tools/reader_bsb.py", \
               "/my_tilers_tools/tiler_functions.py", \
               "/my_tilers_tools/tiles_convert.py", \
               "/my_tilers_tools/tiles_merge_simple.py" ]:
    #print os.path.dirname(__file__)+pyFile, mPath
    copy(os.path.dirname(__file__)+pyFile, mPath)

#copy dependant images
mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/share/mxcart/"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
for pyFile in ["/kattegat.png", "/spinner.gif"]:
    #print os.path.dirname(__file__)+pyFile, mPath
    copy(os.path.dirname(__file__)+pyFile, mPath)

mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/share/icons/hicolor/48x48/apps/"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
copy(os.path.dirname(__file__)+"/mxcart.png", mPath)

#create bin
mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/bin"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
binsh = open(mPath + "/mxcart", "w")
binsh.write("#!/bin/bash\n\n" + \
            "cd /usr/local/lib/mxcart\n" + \
            "python MXCart.py\n")
binsh.close()
Popen(["chmod", "777", mPath + "/mxcart"])

#create desktop entry
mPath = os.path.dirname(__file__)+"/build/debpkg/usr/local/share/applications"
if not os.path.isdir(mPath):
    os.makedirs(mPath)
desktop = open(mPath + "/mxcart.desktop", "w")
desktop.write("[Desktop Entry]\n" + \
    "Version=%s\n" %(versionNum)  + \
    "Name=MX Cart\n" + \
    "Comment=BSB Chart Import Utility\n" + \
    "Path=/usr/local/lib/mxcart/\n" + \
    "Exec=mxcart\n" + \
    "Icon=/usr/local/share/icons/hicolor/48x48/apps/mxcart.png\n" + \
    "StartupNotify=true\n" + \
    "Terminal=false\n" + \
    "Type=Application\n" + \
    "Categories=Education;Science;Geography;" )
desktop.close()

Popen(["dpkg-deb", "-b", os.path.dirname(__file__)+"/build/debpkg", os.path.dirname(__file__)+"/build/MXCart_%s_.deb" %(versionNum)])
##write md5sum file
#mPath = os.path.dirname(__file__)+"/build/debpkg/DEBIAN"
#md5sums = open(mPath+"/md5sums", "w")
#for ea in os.listdir(os.path.dirname(__file__)+"/build/debpkg/usr/local/lib/mxcart/"):
#    fd = open( os.path.dirname(__file__)+"/build/debpkg/usr/local/lib/mxcart/"+ea, "rb" )
#    md5sums.write(md5sum(fd) + "  " + "/usr/local/lib/mxcart/"+ea+"\n")
#    fd.close()
##for fd in os 
#md5sums.close()
