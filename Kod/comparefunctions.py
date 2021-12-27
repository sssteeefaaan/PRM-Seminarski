import datetime as dt
from functools import partial
import ipaddress as ip


def Fsim(a1: tuple, a2: tuple, c: tuple, h: tuple) -> float:
    if len(a1) != len(a2) or len(a1) != len(c) or len(a1) != len(h):
        return 0

    ret = 0.0
    for i in range(0, len(a1)):
        ret += c[i] * h[i](a1[i], a2[i])
    return ret


def equals(a, b):
    if a == b:
        return 1
    return 0


def dateCmp(a, b):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    aD = dt.datetime.strptime(a, '%m/%d/%Y')
    bD = dt.datetime.strptime(b, '%m/%d/%Y')
    delta = aD.__sub__(bD).__abs__()

    return 1 / (1 << (delta.days << 1))


def timeCmp(a, b):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    aD = dt.datetime.strptime(a, '%H:%M:%S')
    bD = dt.datetime.strptime(b, '%H:%M:%S')
    delta = aD.__sub__(bD).__abs__()

    if not (delta.seconds and not 15):
        return 1

    return 1 / (delta.seconds << 6)


def sessionCmp(a, b):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    aD = dt.datetime.strptime(a, '%H:%M:%S')
    bD = dt.datetime.strptime(b, '%H:%M:%S')
    delta = aD.__sub__(bD).__abs__()

    return 1 / (delta.seconds + 1)


def addressCmp(a, b):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    ipA = ip.ip_address(a)
    ipB = ip.ip_address(b)

    rez = int(ipA) - int(ipB)

    return 1 / (abs(rez) + 1)


def addressCmpWithMask(a, b, network=None):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    ipA = ip.ip_address(a)
    ipB = ip.ip_address(b)

    if ipA in network and ipB in network:
        return 1
    return 0


def portCmp(a, b):
    if a == b:
        return 1

    if (not a) or (not b):
        return 0

    return 1 / abs(int(a) - int(b))


funcs = {
    "Fsim": Fsim,
    "equals": equals,
    "dateCmp": dateCmp,
    "timeCmp": timeCmp,
    "sessionCmp": sessionCmp,
    "addressCmp": addressCmp,
    "addressCmpClassA": partial(addressCmpWithMask, network=ip.ip_network("255.0.0.0")),
    "addressCmpClassB": partial(addressCmpWithMask, network=ip.ip_network("255.255.0.0")),
    "addressCmpClassC": partial(addressCmpWithMask, network=ip.ip_network("255.255.255.0")),
    "portCmp": portCmp
}
