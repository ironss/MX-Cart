import platform, os

if platform.system() == "Linux":
        import sys
        sys.path.append(os.path.dirname(os.path.abspath(__file__)) +"/my_tilers_tools")

import tiles_merge_simple

def Merge(dst_dir, src_list):
    if platform.system() == "Windows":
        tiles_merge_simple.set_nothreads()
    tiles_merge_simple.setMergeOptions(src_list)
    src_dirs=[i.rstrip('\n') for i in open(src_list,'r')]
        
    for src in src_dirs:
        if not (src.startswith("#") or src.strip() == ''): # ignore sources with names starting with "#" 
            print src
            print dst_dir
            tiles_merge_simple.MergeSet(src, dst_dir)


if __name__ == "__main__":
    src_list = "c:/users/will/appdata/local/temp/__MXCART/mergeorder.txt"
    dst_dir = "c:/users/will/appdata/local/temp/__MXCART/merge"
    Merge(dst_dir, src_list)
