registers = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "CF": 4,
    "DV": 5,
    "SB": 6,
    "SH": 7,
    "IP": 8,
}


def is_reg(x):
    return x in registers.keys()


def reg(x):
    return registers[x]


def is_const(x):
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


def const(x):
    return eval(x)


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