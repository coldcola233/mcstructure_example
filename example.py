import os
from TrimMCStruct import Block, Structure

def new_filename(filename):
    if not os.path.exists(filename):
        return filename
    basename,postfix = os.path.splitext(filename)
    i = 0
    while True:
        i += 1
        newname = f"{basename}({i}){postfix}"
        if not os.path.exists(newname):
            return newname
        
struct = Structure((4,4,4))
grass = Block("minecraft","grass")
air = Block("minecraft","air")

struct.fill_blocks((0,0,0),(3,3,3),grass)
struct.fill_blocks((2,2,2),(3,3,3),air)

with open(new_filename("out.mcstructure"),"wb") as f:
    struct.dump(f)
