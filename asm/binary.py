from asm.utils import *
from asm.labels import IP


class Binary:
    def __init__(self):
        self.data = "v2.0 raw\n"

    def join(self, word):
        self.data += word.data
        return self


class Word:
    def __init__(self):
        self.num = 0
        self.bit = 0
        self.data = "\n"

    def join(self, bits, data):
        self.num += data << self.bit
        self.bit += bits

        self.data = f"{self.num:x}\n"
        return self

    def size(self, data):
        IP.inc(int(data))
        return self.join(SIZE_IN_WORDS, int(data))

    def opcode(self, data):
        return self.join(OPCODE, int(data))

    def aopcode(self, data):
        return self.join(AOPCODE, aopcodes[data])
    
    def condcode(self, data):
        return self.join(CONDCODE, condcodes[data])

    def reg(self, data):
        return self.join(REGISTER, reg(data))

    def const(self, data):
        return self.join(CONSTANT, const(data))

    def reg_mem(self, data):
        return self.reg(data[1:-1])

    def const_mem(self, data):
        return self.const(data[1:-1])
