import sys


def solution(n, m, k, board):
    answer = -10**9
    b_board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    w_board = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    d = {(0, 'B'): (0, -1), (1, 'W'): (0, -1), (0, 'W'): (-1, 0), (1, 'B'): (-1, 0)}
    for i in range(1, n + 1):
        b, w = 0, 0
        for j in range(1, m + 1):
            b += d[((i + j) % 2, board[i - 1][j - 1])][0]
            w += d[((i + j) % 2, board[i - 1][j - 1])][1]
            b_board[i][j] = b_board[i - 1][j] + b
            w_board[i][j] = w_board[i - 1][j] + w
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            answer = max(answer,
                         b_board[i][j] - b_board[i - k][j] - b_board[i][j - k] + b_board[i - k][j - k],
                         w_board[i][j] - w_board[i - k][j] - w_board[i][j - k] + w_board[i - k][j - k])
    return -answer


N, M, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
B = [sys.stdin.readline().rstrip() for _ in range(N)]
print(solution(N, M, K, B))