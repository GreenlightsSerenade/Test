import sys


def solution(n, m, board):
    DP = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) + board[i - 1][j - 1]
    return DP[n][m]


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
B = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, B))