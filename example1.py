from TrimMCStruct import Block, Structure
with open("cmd.mcstructure","rb") as f:
    struct = Structure.load(f)

cmd = struct.get_block((0,0,0))
print(cmd.states)
print()
print(cmd.extra_data)