from asm.utils import *
from asm.MOV import MOV
from asm.ARITHM import ARITHM


def POP(args, binary):
    if args[0] != 'POP':
        return
    if is_const(args[1]):
        return
    
    print(args, "POP")
    print("\t", end=""), ARITHM(["ADD", "SH", "1"], binary)
    print("\t", end=""), MOV(["MOV", args[1], "[SH]"], binary)

