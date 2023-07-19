from asm.labels import labels

registers = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "RR": 0xFA,
    "RP": 0xFB,
    "CF": 0xFC,
    "SB": 0xFD,
    "SH": 0xFE,
    "IP": 0xFF,
}


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

condcodes = {
    "JE": 0,
    "JNE": 1,
    "JL": 2,
    "JLE": 3,
    "JG": 4,
    "JGE": 5,
    "JMP": 6,
}

def is_condcode(x):
    return x in condcodes.keys()

def condcode(x):
    return condcodes[x]

def is_aopcode(x):
    return x in aopcodes.keys()


def aopcode(x):
    return aopcodes[x]


SIZE_IN_WORDS = 3
OPCODE = 8
AOPCODE = 4
CONDCODE = 3
REGISTER = 8
CONSTANT = 64


def is_reg(x):
    return x in registers.keys()


def reg(x):
    return registers[x]


def is_const(x):
    if is_reg(x):
        return False
    try:
        int(x)
        return True
    except:
        pass
    try:
        int(x, 16)
        return True
    except:
        pass
    try:
        int(x, 2)
        return True
    except:
        pass
    return False


def const(x):
    if isinstance(x, int):
        y = x
    else:
        y = eval(x)
    if y < 0:
        y += 2**64
    return y


def is_reg_mem(x):
    try:
        if x[0] == "[" and x[-1] == "]" and (is_reg(x[1:-1])):
            return True
    except:
        return False
    return False


def is_const_mem(x):
    try:
        if x[0] == "[" and x[-1] == "]" and (is_const(x[1:-1])):
            return True
    except:
        return False
    return False


def mem(x):
    if is_reg(x[1:-1]):
        return reg(x[1:-1])
    return const(x[1:-1])

def is_label(x):
    return x in labels.labels.keys()

def is_label_delc(x):
    try:
        if x[-1] == ':':
            return True
    except:
        pass
    return False
