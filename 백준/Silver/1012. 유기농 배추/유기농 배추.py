import sys


def solution(n, m, board):
    cnt = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            else:
                board[i][j] = 0
                stck = [(i, j)]
                while stck:
                    now = stck.pop()
                    for elem in d:
                        if 0 <= now[0] + elem[0] < n and 0 <= now[1] + elem[1] < m:
                            if board[now[0] + elem[0]][now[1] + elem[1]] == 1:
                                stck.append((now[0] + elem[0], now[1] + elem[1]))
                                board[now[0] + elem[0]][now[1] + elem[1]] = 0
                cnt += 1
    return cnt


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    B = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
        B[y][x] = 1
    print(solution(N, M, B))