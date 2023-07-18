from asm.utils import *


def DONE(args, add_words):
    if args[0] != "DONE":
        return
    word = 1  # size in words
    word += 255 << (3)  # opcode

    add_words(word)
