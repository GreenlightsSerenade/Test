import sys


def fact(n, p):
    ret = 1
    for i in range(1, n + 1):
        ret = (ret * i) % p
    return ret % p


def sq(x, y, z):
    if y == 2:
        return (x * x) % z
    elif y == 1:
        return x % z

    tmp = sq(x, y // 2, z)
    if y % 2 == 0:
        return (tmp * tmp) % z
    else:
        return (tmp * tmp * x) % z


def solution(n, k):
    p = 1000000007

    return (fact(n, p) * sq(fact(n - k, p) * fact(k, p), p - 2, p)) % p


N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, K))