from asm.utils import *

aopcodes = {
    "ADD": 0,
    "SUB": 1,
    "MUL": 2,
    "DIVQ": 3,
    "DIVR": 4,
    "AND": 5,
    "OR": 6,
    "XOR": 7,
    "NOT": 8,
    "SHL": 9,
    "SHR": 10,
}

def is_aopcode(x):
    return x in aopcodes.keys()

def aopcode(x):
    return aopcodes[x]


def ARITHM_OP_reg_reg(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "ARITHM_OP_reg_reg")

    word = 1  # size in words
    word += 8 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += reg(args[1]) << (3 + 8 + 4)  # register 1
    word += reg(args[2]) << (3 + 8 + 4 + 8)  # register 2

    add_words(word)


def ARITHM_OP_reg_const(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_reg_const")

    word = 2  # size in words
    word += 9 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += reg(args[1]) << (3 + 8 + 4)  # reg

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def ARITHM_OP_reg_MEMconst(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "ARITHM_OP_reg_MEMconst")

    word = 2  # size in words
    word += 10 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += reg(args[1]) << (3 + 8 + 4)  # reg

    add_words(word)

    word = mem(args[2])  # const

    add_words(word)


def ARITHM_OP_reg_MEMreg(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return

    print(args, "ARIHTM_OP_reg_MEMreg")

    word = 1  # size in words
    word += 11 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += reg(args[1]) << (3 + 8 + 4)  # reg
    word += mem(args[2]) << (3 + 8 + 4 + 8)  # mem

    add_words(word)


def ARITHM_OP_MEMconst_const(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_MEMconst_const")

    word = 3  # size in words
    word += 12 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def ARITHM_OP_MEMconst_reg(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "ARITHM_OP_MEMconst_reg")

    word = 2  # size in words
    word += 13 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += reg(args[2]) << (3 + 8 + 4)  # reg

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)


def ARITHM_OP_MEMreg_const(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_MEMreg_const")

    word = 2  # size in words
    word += 14 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += mem(args[1]) << (3 + 8 + 4)  # mem

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def ARITHM_OP_MEMreg_reg(args, add_words):
    if not is_aopcode(args[0]):
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "ARITHM_OP_MEMreg_reg")

    word = 1  # size in words
    word += 15 << (3)  # opcode
    word += aopcode(args[0]) << (3 + 8)  # aopcode
    word += mem(args[1]) << (3 + 8 + 4)  # mem
    word += reg(args[2]) << (3 + 8 + 4 + 8)  # mem

    add_words(word)


def ARITHM(args, add_words):
    ARITHM_OP_reg_reg(args, add_words)
    ARITHM_OP_reg_const(args, add_words)
    ARITHM_OP_reg_MEMconst(args, add_words)
    ARITHM_OP_reg_MEMreg(args, add_words)
    ARITHM_OP_MEMconst_const(args, add_words)
    ARITHM_OP_MEMconst_reg(args, add_words)
    ARITHM_OP_MEMreg_const(args, add_words)
    ARITHM_OP_MEMreg_reg(args, add_words)
