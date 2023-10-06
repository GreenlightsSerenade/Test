import sys


def solution(n, mtxs):
    DP = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(n - i):
            DP[j][i + j] = float('INF')
            for k in range(j, i + j):
                DP[j][i + j] = min(DP[j][i + j], DP[j][k] + DP[k + 1][i + j]
                                   + mtxs[j][0] * mtxs[k][1] * mtxs[i + j][1])
    return DP[0][-1]


N = int(sys.stdin.readline().rstrip())
L = [tuple(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, L))