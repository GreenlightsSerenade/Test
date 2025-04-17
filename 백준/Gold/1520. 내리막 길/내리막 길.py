import sys
from collections import deque, defaultdict
from itertools import combinations
import heapq
sys.setrecursionlimit(10 ** 8)

def solution(n, m, g):
    dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    DP = [[-1 for _ in range(m)] for _ in range(n)]

    def DFS(nx, ny):
        if nx == n - 1 and ny == m - 1:
            return 1
        if DP[nx][ny] != -1:
            return DP[nx][ny]

        ret = 0
        for dx, dy in dxdy:
            x, y = nx + dx, ny + dy
            if 0 <= x < n and 0 <= y < m and g[nx][ny] > g[x][y]:
                ret += DFS(x, y)

        DP[nx][ny] = ret
        return DP[nx][ny]

    return DFS(0, 0)


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, L))