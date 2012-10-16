import platform, os

if platform.system() == "Linux":
        import sys
        sys.path.append(os.path.dirname(os.path.abspath(__file__)) +"/my_tilers_tools")

from gdal_tiler import main, set_nothreads

def VrtToTiles(tempDir, vrtPath, zoomLevel):
    options = []
    #options.append(os.path.dirname(__file__)+"/gdal_tiler.py")
    options.append('--overview-resampling=bilinear')
    options.append('--base-resampling=bilinear')
    options.append('-t')
    options.append(tempDir)
    options.append('-c')
    options.append(vrtPath)
    options.append('-z')
    options.append(str(zoomLevel))
    if platform.system() == "Windows":
        set_nothreads()
    main(options)
    
if __name__ == "__main__":
    VrtToTiles('/tmp/__MXCART', '/home/will/zxyCharts/BSB_ROOT/NOAA_BSB_ROOT/BSB_ROOT/1113A/1113A_1.vrt', 11)