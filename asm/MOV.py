from asm.utils import *


def MOV_reg_reg(args, add_words):
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

    add_words(word)


def MOV_reg_const(args, add_words):
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

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def MOV_reg_MEMconst(args, add_words):
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

    add_words(word)

    word = mem(args[2])  # const

    add_words(word)


def MOV_reg_MEMreg(args, add_words):
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

    add_words(word)


def MOV_MEMconst_const(args, add_words):
    if args[0] != "MOV":
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "MOV_MEMconst_const")

    word = 3  # size in words
    word += 4 << (3)  # opcode

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)

    word = const(args[2])  # const

    data += f"{word:x}\n"


def MOV_MEMconst_reg(args, add_words):
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

    add_words(word)

    word = mem(args[1])  # mem

    add_words(word)


def MOV_MEMreg_const(args, add_words):
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

    add_words(word)

    word = const(args[2])  # const

    add_words(word)


def MOV_MEMreg_reg(args, add_words):
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

    add_words(word)


def MOV(args, add_words):
    MOV_reg_reg(args, add_words)
    MOV_reg_const(args, add_words)
    MOV_reg_MEMconst(args, add_words)
    MOV_reg_MEMreg(args, add_words)
    MOV_MEMconst_const(args, add_words)
    MOV_MEMconst_reg(args, add_words)
    MOV_MEMreg_const(args, add_words)
    MOV_MEMreg_reg(args, add_words)
