import random
from time import time
from tabulate import tabulate


def isPrime(p):
    for n in range(2, int(p ** 1 / 2) + 1):
        if p % n == 0:
            return False
    return True


def nBitPrime(n):
    # Generate a random float  between 0.0 and 1.0
    x = random.random()
    # print('x = ', x)

    # Then multiply it by 2**n to get a random number in the range we are interested in
    y = int(x * (2 ** n))
    # print('y=', y)

    # If this number is >= 2 and prime, then return it
    if isPrime(y):
        # print(y)
        return y
    else:
        return nBitPrime(n)


def factor(pq):
    print("\nFactors of", pq)
    i = 2
    while i < pq:
        if pq % i == 0:
            print(i)
        i = i + 1


table = {}
for n in range(15, 16):
    pq = nBitPrime(n) * nBitPrime(n)

    t1 = time()
    factor(pq)
    t2 = time()
    factorTime = (t2 - t1)
    print('Factor Time = ', factorTime)
    table[n] = round(factorTime, 1)

headers = ['i', 'Time(sec)']
print(tabulate([(k,) + v for k, v in table.items()], headers=headers))


# For a 1024-bit key, it would take:
# 365481365481233.3 milliseconds
# 101.5 hours
# 4.23 days
# 0.01 years
