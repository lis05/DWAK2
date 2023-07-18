from asm.utils import *


def CMP_reg_reg(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "CMP_reg_reg")

    word = 1  # size in words
    word += 16 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # register 1
    word += reg(args[2]) << (3 + 8 + 8)  # register 2

    add_words(word)


def CMP_reg_const(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_reg_const")

    word = 2  # size in words
    word += 17 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def CMP_reg_MEMconst(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "CMP_reg_MEMconst")

    word = 2  # size in words
    word += 18 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg

    add_words(word)

    word = mem(args[2])  # const

    add_words(word)


def CMP_reg_MEMreg(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return

    print(args, "CMP_reg_MEMreg")

    word = 1  # size in words
    word += 19 << (3)  # opcode
    word += reg(args[1]) << (3 + 8)  # reg
    word += mem(args[2]) << (3 + 8 + 8)  # mem

    add_words(word)


def CMP_MEMconst_const(args, add_words):
    if args[0] != "CMP":
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_MEMconst_const")

    word = 3  # size in words
    word += 20 << (3)  # opcode

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def CMP_MEMconst_reg(args, add_words):
    if args[0] != "CMP":
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "CMP_MEMconst_reg")

    word = 2  # size in words
    word += 21 << (3)  # opcode
    word += reg(args[2]) << (3 + 8)  # reg

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)


def CMP_MEMreg_const(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_MEMreg_const")

    word = 2  # size in words
    word += 22 << (3)  # opcode
    word += mem(args[1]) << (3 + 8)  # mem

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def CMP_MEMreg_reg(args, add_words):
    if args[0] != "CMP":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "CMP_MEMreg_reg")

    word = 1  # size in words
    word += 23 << (3)  # opcode
    word += mem(args[1]) << (3 + 8)  # mem
    word += reg(args[2]) << (3 + 8 + 8)  # mem

    add_words(word)


def CMP_const_const(args, add_words):
    if args[0] != "CMP":
        return
    if not is_const(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_const_const")

    word = 3  # size in words
    word += 24 << (3)  # opcode

    add_words(word)

    word = const(args[1])

    add_words(word)

    word = const(args[2])

    add_words(word)


def CMP(args, add_words):
    CMP_reg_reg(args, add_words)
    CMP_reg_const(args, add_words)
    CMP_reg_MEMconst(args, add_words)
    CMP_reg_MEMreg(args, add_words)
    CMP_MEMconst_const(args, add_words)
    CMP_MEMconst_reg(args, add_words)
    CMP_MEMreg_const(args, add_words)
    CMP_MEMreg_reg(args, add_words)
    CMP_const_const(args, add_words)
