from asm.utils import *
from asm.binary import Word


def MOV_reg_reg(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "MOV_reg_reg")

    binary.join(Word().size(1).opcode(0).reg(args[1]).reg(args[2]))


def MOV_reg_const(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "MOV_reg_const")

    binary.join(Word().size(2).opcode(1).reg(args[1]))
    binary.join(Word().const(args[2]))


def MOV_reg_MEMconst(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "MOV_reg_MEMconst")

    binary.join(Word().size(2).opcode(2).reg(args[1]))
    binary.join(Word().const_mem(args[2]))


def MOV_reg_MEMreg(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return

    print(args, "MOV_reg_MEMreg")

    binary.join(Word().size(1).opcode(3).reg(args[1]).reg_mem(args[2]))


def MOV_MEMconst_const(args, binary):
    if args[0] != "MOV":
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "MOV_MEMconst_const")

    binary.join(Word().size(3).opcode(4))
    binary.join(Word().const_mem(args[1]))
    binary.join(Word().const(args[2]))


def MOV_MEMconst_reg(args, binary):
    if args[0] != "MOV":
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "MOV_MEMconst_reg")

    binary.join(Word().size(2).opcode(5).reg(args[2]))
    binary.join(Word().const_mem(args[1]))


def MOV_MEMreg_const(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "MOV_MEMreg_const")

    binary.join(Word().size(2).opcode(6).reg_mem(args[1]))
    binary.join(Word().const(args[2]))


def MOV_MEMreg_reg(args, binary):
    if args[0] != "MOV":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "MOV_MEMreg_reg")

    binary.join(Word().size(1).opcode(7).reg_mem(args[1]).reg(args[2]))

def MOV(args, binary):
    MOV_reg_reg(args, binary)
    MOV_reg_const(args, binary)
    MOV_reg_MEMconst(args, binary)
    MOV_reg_MEMreg(args, binary)
    MOV_MEMconst_const(args, binary)
    MOV_MEMconst_reg(args, binary)
    MOV_MEMreg_const(args, binary)
    MOV_MEMreg_reg(args, binary)
