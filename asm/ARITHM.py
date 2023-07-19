from asm.utils import *
from asm.binary import Word


def ARITHM_OP_reg_reg(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]) or not is_reg(args[2]):
        return
    if args[1] == args[2]:
        return

    print(args, "ARITHM_OP_reg_reg")

    binary.join(Word().size(1).opcode(8).aopcode(args[0]).reg(args[1]).reg(args[2]))


def ARITHM_OP_reg_const(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_reg_const")

    binary.join(Word().size(2).opcode(9).aopcode(args[0]).reg(args[1]))
    binary.join(Word().const(args[2]))


def ARITHM_OP_reg_MEMconst(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_const_mem(args[2]):
        return

    print(args, "ARITHM_OP_reg_MEMconst")

    binary.join(Word().size(2).opcode(10).aopcode(args[0]).reg(args[1]))
    binary.join(Word().const_mem(args[2]))


def ARITHM_OP_reg_MEMreg(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    if not is_reg_mem(args[2]):
        return

    print(args, "ARIHTM_OP_reg_MEMreg")

    binary.join(Word().size(1).opcode(11).aopcode(args[0]).reg(args[1]).reg_mem(args[2]))


def ARITHM_OP_MEMconst_const(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_const_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_MEMconst_const")

    binary.join(Word().size(3).opcode(12).aopcode(args[0]))
    binary.join(Word().const_mem(args[1]))
    binary.join(Word().const(args[2]))


def ARITHM_OP_MEMconst_reg(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_const_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "ARITHM_OP_MEMconst_reg")

    binary.join(Word().size(2).opcode(13).aopcode(args[0]).reg(args[2]))
    binary.join(Word().const_mem(args[1]))


def ARITHM_OP_MEMreg_const(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg_mem(args[1]):
        return
    if not is_const(args[2]):
        return

    print(args, "ARITHM_OP_MEMreg_const")

    binary.join(Word().size(2).opcode(14).aopcode(args[0]).reg_mem(args[1]))
    binary.join(Word().const(args[2]))


def ARITHM_OP_MEMreg_reg(args, binary):
    if not is_aopcode(args[0]):
        return
    if not is_reg_mem(args[1]):
        return
    if not is_reg(args[2]):
        return

    print(args, "ARITHM_OP_MEMreg_reg")

    binary.join(Word().size(1).opcode(15).aopcode(args[0]).reg_mem(args[1]).reg(args[2]))


def ARITHM(args, binary):
    ARITHM_OP_reg_reg(args, binary)
    ARITHM_OP_reg_const(args, binary)
    ARITHM_OP_reg_MEMconst(args, binary)
    ARITHM_OP_reg_MEMreg(args, binary)
    ARITHM_OP_MEMconst_const(args, binary)
    ARITHM_OP_MEMconst_reg(args, binary)
    ARITHM_OP_MEMreg_const(args, binary)
    ARITHM_OP_MEMreg_reg(args, binary)
