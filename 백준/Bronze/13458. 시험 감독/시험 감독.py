import sys


def solution(n, peo, b, c):
    ans = 0
    for elem in peo:
        base = 0 if (elem - b) <= 0 else (elem - b - 1) // c + 1
        ans = ans + 1 + base
    return ans


N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
B, C = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, L, B, C))
