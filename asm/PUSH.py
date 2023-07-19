from asm.utils import *
from asm.MOV import MOV
from asm.ARITHM import ARITHM


def PUSH(args, binary):
    if args[0] != 'PUSH':
        return
    print(args, "PUSH")
    print("\t", end=""), MOV(["MOV", "[SH]", args[1]], binary)
    print("\t", end=""), ARITHM(["SUB", "SH", "1"], binary)

