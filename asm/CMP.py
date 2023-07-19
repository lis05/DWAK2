from asm.utils import *
from asm.binary import Word


def CMP_reg_reg(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "CMP_reg_reg")

    binary.join(Word().size(1).opcode(16).reg(args[1]).reg(args[2]))


def CMP_reg_const(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_reg_const")

    binary.join(Word().size(2).opcode(17).reg(args[1]))
    binary.join(Word().const(args[2]))


def CMP_reg_MEMconst(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "CMP_reg_MEMconst")

    binary.join(Word().size(2).opcode(18).reg(args[1]))
    binary.join(Word().const_mem(args[2]))


def CMP_reg_MEMreg(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return

    print(args, "CMP_reg_MEMreg")

    binary.join(Word().size(1).opcode(19).reg(args[1]).reg_mem(args[2]))


def CMP_MEMconst_const(args, binary):
    if args[0] != "CMP":
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_MEMconst_const")

    binary.join(Word().size(3).opcode(20))
    binary.join(Word().const_mem(args[1]))
    binary.join(Word().const(args[2]))


def CMP_MEMconst_reg(args, binary):
    if args[0] != "CMP":
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "CMP_MEMconst_reg")

    binary.join(Word().size(2).opcode(21).reg(args[2]))
    binary.join(Word().const_mem(args[1]))


def CMP_MEMreg_const(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_MEMreg_const")

    binary.join(Word().size(2).opcode(22).reg_mem(args[1]))
    binary.join(Word().const(args[2]))


def CMP_MEMreg_reg(args, binary):
    if args[0] != "CMP":
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "CMP_MEMreg_reg")

    binary.join(Word().size(1).opcode(23).reg_mem(args[1]).reg(args[2]))


def CMP_const_const(args, binary):
    if args[0] != "CMP":
        return
    if not is_const(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "CMP_const_const")

    binary.join(Word().size(3).opcode(24))
    binary.join(Word().const(args[1]))
    binary.join(Word().const(args[2]))


def CMP(args, binary):
    CMP_reg_reg(args, binary)
    CMP_reg_const(args, binary)
    CMP_reg_MEMconst(args, binary)
    CMP_reg_MEMreg(args, binary)
    CMP_MEMconst_const(args, binary)
    CMP_MEMconst_reg(args, binary)
    CMP_MEMreg_const(args, binary)
    CMP_MEMreg_reg(args, binary)
    CMP_const_const(args, binary)
