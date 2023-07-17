#!/bin/python3
import sys

program = sys.argv[1]
output = sys.argv[2]

data = "v2.0 raw\n"


with open(program, "r") as f:
    lines = f.readlines()


for i in range(len(lines)):
    lines[i] = lines[i].replace(", ", " ").replace("\n", " ")
    lines[i] = lines[i].replace("\t", " ")

# =========
registers = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "CF": 4,
    "DV": 5,
    "SB": 6,
    "SH": 7,
    "IP": 8,
}


def is_reg(x):
    return x in registers.keys()


def reg(x):
    return registers[x]


def is_const(x):
    try:
        int(x)
        return True
    except:
        pass
    try:
        int(x, 16)
        return True
    except:
        pass
    try:
        int(x, 2)
        return True
    except:
        pass


def const(x):
    return eval(x)


def is_reg_mem(x):
    try:
        if x[0] == "[" and x[-1] == "]" and (is_reg(x[1:-1])):
            return True
    except:
        return False
    return False


def is_const_mem(x):
    try:
        if x[0] == "[" and x[-1] == "]" and (is_const(x[1:-1])):
            return True
    except:
        return False
    return False


def mem(x):
    if is_reg(x[1:-1]):
        return reg(x[1:-1])
    return const(x[1:-1])


def MOV_reg_reg(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "MOV_reg_reg")

    word = 1  # size in words
    word += 0 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # register 1
    word += reg(args[2]) << (3 + 8 + 8)  # register 2

    data += f"{word:x}\n"


def MOV_reg_const(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "MOV_reg_const")

    word = 2  # size in words
    word += 1 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg

    data += f"{word:x}\n"

    word = const(args[2])  # const

    data += f"{word:x}\n"


def MOV_reg_MEMconst(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "MOV_reg_MEMconst")

    word = 2  # size in words
    word += 2 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg

    data += f"{word:x}\n"

    word = mem(args[2])  # const

    data += f"{word:x}\n"


def MOV_reg_MEMreg(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return
    
    print(args, "MOV_reg_MEMreg")

    word = 1  # size in words
    word += 3 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg
    word += mem(args[2]) << (3 + 8 + 8)  # mem

    data += f"{word:x}\n"


def MOV_MEMconst_const(args):
    global data
    if args[0] != "MOV":
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return
    
    print(args, "MOV_MEMconst_const")

    word = 3  # size in words
    word += 4 << (3)  # opcode

    data += f"{word:x}\n"

    word = mem(args[1])  # mem

    data += f"{word:x}\n"

    word = const(args[2])  # const

    data += f"{word:x}\n"


def MOV_MEMconst_reg(args):
    global data
    if args[0] != "MOV":
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return
    
    print(args, "MOV_MEMconst_reg")

    word = 2  # size in words
    word += 5 << (3)  # opcode
    word += reg(args[2]) << (3 + 8)  # reg

    data += f"{word:x}\n"

    word = mem(args[1])  # mem

    data += f"{word:x}\n"


def MOV_MEMreg_const(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return
    
    print(args, "MOV_MEMreg_const")

    word = 2  # size in words
    word += 6 << (3)  # opcode
    word += mem(args[1]) << (3 + 8)  # mem

    data += f"{word:x}\n"

    word = const(args[2])  # const

    data += f"{word:x}\n"


def MOV_MEMreg_reg(args):
    global data
    if args[0] != "MOV":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return
    
    print(args, "MOV_MEMreg_reg")

    word = 1  # size in words
    word += 7 << (3)  # opcode
    word += mem(args[1]) << (3 + 8)  # mem
    word += reg(args[2]) << (3 + 8 + 8)  # mem

    data += f"{word:x}\n"


def DONE(args):
    global data
    if args[0] != "DONE":
        return
    word = 1  # size in words
    word += 255 << (3)  # opcode

    data += f"{word:x}\n"


for line in lines:
    args = line.split()

    if not args: continue

    MOV_reg_reg(args)
    MOV_reg_const(args)
    MOV_reg_MEMconst(args)
    MOV_reg_MEMreg(args)
    MOV_MEMconst_const(args)
    MOV_MEMconst_reg(args)
    MOV_MEMreg_const(args)
    MOV_MEMreg_reg(args)
    DONE(args)

with open(output, "w") as f:
    f.write(data)
