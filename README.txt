Python modules

cx_freeze http://cx-freeze.sourceforge.net/
gdal http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
python image library http://www.pythonware.com/products/pil/
pyproj http://code.google.com/p/pyproj/downloads/list
shapely http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely

****************************************************************

Note for cx_freeze on Windows the following hack is required:
cx_freeze will not find pyproj data folder in zip file.

modify __init__ file of pyproj as follows and copy data dir to MXCart root directory

pyproj_datadir = os.sep.join([os.path.abspath(os.path.dirname(__file__)+"/../../"), 'data'])

also change the following in tilers_tools/tiler_functions:

def data_dir():
    return os.path.dirname(__file__)+"/../"
    #return sys.path[0]
    
Lastly, reader_bsb_data.csv needs to be copied to cx_freeze build directory

****************************************************************

gdal_tiler.py line 470 change to...

'band_list':band_lst.encode('utf-8'),