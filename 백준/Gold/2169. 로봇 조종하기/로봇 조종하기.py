import sys
from collections import deque, defaultdict
from itertools import combinations
import heapq


def solution(n, m, g):
    DP = [[0 for i in range(m)] for j in range(n)]
    tmp = [[0, 0] for i in range(m)]
    for i in range(m):
        DP[0][i] = DP[0][i - 1] + g[0][i]

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                tmp[j][0] = DP[i - 1][j] + g[i][j]
                tmp[-j-1][1] = DP[i - 1][-j - 1] + g[i][-j-1]
            else:
                tmp[j][0] = max(DP[i - 1][j], tmp[j - 1][0]) + g[i][j]
                tmp[-j-1][1] = max(DP[i - 1][-j - 1], tmp[-j][1]) + g[i][-j-1]
        for j in range(m):
            DP[i][j] = max(tmp[j])
    return DP[-1][-1]


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, L))