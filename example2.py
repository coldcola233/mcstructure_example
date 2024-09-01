from TrimMCStruct import Block, Structure
import os

def command_block(
    type:str,
    command:str,
    TickDelay:int = 0,
    auto:bool = True,
    conditional_bit:bool = False,
    facing_direction:int = 1
):

    return Block(
        "minecraft",
        type,
        {
            "conditional_bit": conditional_bit,
            "facing_direction": facing_direction
        },
        {
            "block_entity_data": {
                "Command": command,
                "CustomName": "",
                "ExecuteOnFirstTick": 0,
                "LPCommandMode": 0,
                "LPCondionalMode": 0,
                "LPRedstoneMode": 0,
                "LastExecution": 0,
                "LastOutput": "",
                "LastOutputParams": [],
                "SuccessCount": 0,
                "TickDelay": TickDelay,       # 延迟
                "TrackOutput": 1,
                "Version": 35,           
                "auto": auto,              # 保持开启
                "conditionMet": 0,
                "conditionalMode": conditional_bit,   # 是否有条件
                "id": "CommandBlock",   # 下面的不用改
                "isMovable": 1,
                "powered": 0,
                "x": 0,
                "y": 0,
                "z": 0
            }
        }
    )  

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


with open("a.txt") as f:
    cmd = [
          i.strip() for i in f.readlines()
            if i.strip() and not i.startswith("#")
          ]

struct = Structure((1,len(cmd),1))

for i in range(len(cmd)):
    struct.set_block(
        (0,i,0),
        command_block(
            "chain_command_block",
            cmd[i],
            True
        )
    )
with open(new_filename("cmd_out.mcstructure"),"wb") as f:
    struct.dump(f)
