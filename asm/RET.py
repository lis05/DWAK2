from asm.utils import *
from asm.MOV import MOV
from asm.ARITHM import ARITHM
from asm.POP import POP
from asm.JMP import JMP
from asm.labels import IP


def RET(args, binary):
    if args[0] != 'RET':
        return
    
    print(args, "RET")
    print("\t", end=""), POP(["POP", "RP"], binary)
    print("\t", end=""), POP(["POP", "CF"], binary)
    print("\t", end=""), POP(["POP", "R3"], binary)
    print("\t", end=""), POP(["POP", "R2"], binary)
    print("\t", end=""), POP(["POP", "R1"], binary)
    print("\t", end=""), POP(["POP", "R0"], binary)
    print("\t", end=""), POP(["POP", "SB"], binary)
    print("\t", end=""), POP(["POP", "SH"], binary)
    
    print("\t", end=""), JMP(["JMP", "RP"], binary)


