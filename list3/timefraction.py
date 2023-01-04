from random import random


def approx_pn(_n):
    S = 0
    _L = 0
    for N in range(1, _n+1):
        x = 0
        while x == 0:
            x = random() * 2 - 1
        if x < 0:
            x = -1
        else:
            x = 1
        S += x
        if S >= 0:
            _L += 1
    return _L


start = time()
P100 = []
P1000 = []
P10000 = []
for k in range(5000):
    L = approx_pn(100)
    P100.append(L/100)
    L = approx_pn(1000)
    P1000.append(L / 1000)
    L = approx_pn(10000)
    P10000.append(L / 10000)
