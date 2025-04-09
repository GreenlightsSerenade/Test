import sys
from collections import deque


def solution(N, cost):
    DP = [0 for _ in range(N)]
    for i in range(N):
        t, p = cost[-1 - i]
        if t - i <= 1:
            DP[i] = max(p + DP[i - t], DP[i - 1])
        else:
            DP[i] = max(0, DP[i - 1])
    return DP[-1]


N = int(sys.stdin.readline().rstrip())
C = []
for _ in range(N):
    t, p = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    C.append((t, p))
print(solution(N, C))