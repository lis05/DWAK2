#!/bin/python3
import sys
import asm


program = sys.argv[1]
output = sys.argv[2]

data = "v2.0 raw\n"


with open(program, "r") as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].replace(", ", " ").replace("\n", " ")
    lines[i] = lines[i].replace("\t", " ")

# ========

def add_words(*words):
    global data
    for w in words:
        data += f"{w:x}\n"


for line in lines:
    args = line.split()
    if not args: continue

    asm.MOV.MOV(args, add_words)
    asm.ARITHM.ARITHM(args, add_words)
    asm.CMP.CMP(args, add_words)
    asm.DONE.DONE(args, add_words)

with open(output, "w") as f:
    f.write(data)
