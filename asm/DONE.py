from asm.utils import *
from asm.binary import Word


def DONE(args, binary):
    if args[0] != "DONE":
        return

    print(args, "DONE")

    binary.join(Word().size(1).opcode(255))
