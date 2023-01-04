from random import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss
from sortedcontainers import SortedDict


def cdf_approx(_n):
    allsn = []
    for k in range(5000):
        sn = 0
        for n in range(_n):
            x = 0
            while x == 0:
                x = random() * 2 - 1
            if x < 0:
                x = -1
            else:
                x = 1
            sn += x
        allsn.append(sn)
    sndict = {}
    for s in allsn:
        if s in sndict.keys():
            sndict[s] += 1
        else:
            sndict[s] = 1

    # histogram
    od = SortedDict(sndict)
    mylist = [key for key, val in od.items() for _ in range(val)]
    plt.hist(mylist, bins=len(od.keys()))
    plt.title(f"Hist S_{_n}")
    plt.show()

    # dystrybuanta
    cdf = sndict.copy()
    for t in sndict.keys():
        for j in sndict.keys():
            if t > j:
                cdf[t] += sndict[j]
    x = [int(i) for i in sndict.keys()]
    y = [i / 5000 for i in cdf.values()]
    plt.scatter(x, y)
    plt.title(f"S_{_n} CDF")
    plt.ylabel("CDF")
    plt.xlabel("x")
    plt.show()


for N in range(5, 31, 5):
    cdf_approx(N)
cdf_approx(100)

# dystrybuanta rozkladu normalnego
x2 = np.linspace(-4, 4, 1000)
y2 = ss.norm.cdf(x2)
plt.plot(x2, y2, color='red')
plt.title('Normal CDF')
plt.xlabel('x')
plt.ylabel('CDF')
plt.show()
