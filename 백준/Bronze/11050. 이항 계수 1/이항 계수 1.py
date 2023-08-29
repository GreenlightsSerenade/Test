import sys

def facto(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret

def comb(n, k):
    return facto(n) // (facto(n - k) * facto(k))

n, k = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(comb(n, k))
