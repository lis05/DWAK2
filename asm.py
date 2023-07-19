#!/bin/python3
import sys, os
import asm
from asm.labels import IP

program = sys.argv[1]
output = sys.argv[2]

binary = asm.binary.Binary()


with open(program, "r") as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].replace(", ", " ").replace("\n", " ")
    lines[i] = lines[i].replace("\t", " ")

# =======

N = 5
for x in range(N):
    IP.IP = 0
    if x != N-1: sys.stdout = open(os.devnull, 'w')
    if x == N-1: sys.stdout = sys.__stdout__
    for line in lines:
        args = line.split()
        if not args:
            continue

        asm.JMP.JMP(args, binary) # labels are checked here
        asm.MOV.MOV(args, binary)
        asm.ARITHM.ARITHM(args, binary)
        asm.CMP.CMP(args, binary)
        asm.PUSH.PUSH(args, binary)
        asm.POP.POP(args, binary)
        asm.CALL.CALL(args, binary)
        asm.RET.RET(args, binary)
        asm.DONE.DONE(args, binary)
    
    if x != N-1:
        binary.data = "v2.0 raw\n"

with open(output, "w") as f:
    f.write(binary.data)
