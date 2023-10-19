import sys


def solution(x, y, a, b):
    return (x // (a + 1) + (1 if x % (a + 1) else 0)) * (y // (b + 1) + (1 if y % (b + 1) else 0))


H, W, N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(H, W, N, M))