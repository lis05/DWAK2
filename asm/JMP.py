from asm.utils import *
from asm.binary import Word
from asm.labels import labels, IP

def JMP_label(args):
    if is_label_delc(args[0]):
        print("Detected label declaration: %s at address %s" % (args[0][:-1], IP.IP))
        labels.add(args[0][:-1])
    
    for i in range(len(args)):
        if args[i] == "//": break
        if is_label(args[i]):
            args[i] = str(labels.get(args[i]))
        if args[i][0] == '[' and args[i][-1] == ']' and is_label(args[i][1:-1]):
            args[i] = "[%s]" % str(labels.get(args[i]))

def JMP_const(args, binary):
    if not is_condcode(args[0]):
        return
    if not is_const(args[1]):
        return
    
    print(args, "JMP_const")

    binary.join(Word().size(2).opcode(25).condcode(args[0]))
    binary.join(Word().const(args[1]))

def JMP_reg(args, binary):
    if not is_condcode(args[0]):
        return
    if not is_reg(args[1]):
        return
    
    print(args, "JMP_reg")

    binary.join(Word().size(1).opcode(26).condcode(args[0]).reg(args[1]))

def JMP_MEMconst(args, binary):
    if not is_condcode(args[0]):
        return
    if not is_const_mem(args[1]):
        return
    
    print(args, "JMP_MEMconst")

    binary.join(Word().size(2).opcode(27).condcode(args[0]))
    binary.join(Word().const_mem(args[1]))

def JMP_MEMreg(args, binary):
    if not is_condcode(args[0]):
        return
    if not is_reg_mem(args[1]):
        return
    
    print(args, "JMP_reg")

    binary.join(Word().size(1).opcode(28).condcode(args[0]).reg_mem(args[1]))

def JMP(args, binary):
    JMP_label(args)
    JMP_const(args, binary)
    JMP_reg(args, binary)
    JMP_MEMconst(args, binary)
    JMP_MEMreg(args, binary)
