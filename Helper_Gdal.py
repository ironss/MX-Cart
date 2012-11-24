import platform, os

if platform.system() == "Linux":
        import sys
        sys.path.append(os.path.dirname(os.path.abspath(__file__)) +"/my_tilers_tools")

from reader_bsb import BsbKapMap

class options:
    def __init__(self):
        self.srs = None
        self.proj = None
        self.datum = None
        self.force_dtm = None
        self.dtm_shift = None
        self.after_name = None
        self.after_map = None
        self.dst_dir = None
        self.long_name = None
        self.get_cutline = None
        self.cut_file = None

def KapToVrt(kapPath):
    try:
        for overlay in BsbKapMap(kapPath, options()).get_layers():
            overlay.convert()
        
    except:
        return False
    
    return True

if __name__ == "__main__":        
    #print KapToVrt("C:/Users/will/Desktop/simcoe/2028B01.KAP")
    #print KapToVrt("/home/will/zxyCharts/BSB_ROOT/NOAA_BSB_ROOT/BSB_ROOT/1113A/1113A_1.KAP")
    print KapToVrt("/home/will/zxyCharts/BSB_ROOT/shom/CD1/Samso Kattegat/N0S26_1.kap")




