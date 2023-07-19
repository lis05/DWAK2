from asm.utils import *
from asm.MOV import MOV
from asm.ARITHM import ARITHM
from asm.PUSH import PUSH
from asm.JMP import JMP
from asm.labels import IP


def CALL(args, binary):
    if args[0] != 'CALL':
        return
    
    print(args, "CALL")
    print("\t", end=""), PUSH(["PUSH", "SH"], binary)
    print("\t", end=""), PUSH(["PUSH", "SB"], binary)
    print("\t", end=""), PUSH(["PUSH", "R0"], binary)
    print("\t", end=""), PUSH(["PUSH", "R1"], binary)
    print("\t", end=""), PUSH(["PUSH", "R2"], binary)
    print("\t", end=""), PUSH(["PUSH", "R3"], binary)
    print("\t", end=""), PUSH(["PUSH", "CF"], binary)
    ip = IP.IP + 8
    if is_reg(args[1]):
        ip -= 1
    print("\t", end=""), MOV(["MOV", "RP", str(ip)], binary)
    print("\t", end=""), PUSH(["PUSH", "RP"], binary)
    print("\t", end=""), MOV(["MOV", "SB", "SH"], binary)
    print("\t", end=""), JMP(["JMP", args[1]], binary)




