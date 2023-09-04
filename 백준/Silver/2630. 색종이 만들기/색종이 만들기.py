import sys


def recur(n, x, y, board):
    if n == 1:
        if board[x][y] == 0:
            return (1, 0)
        else:
            return (0, 1)

    tmp = board[x][y]
    flag = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tmp != board[i][j]:
                flag = False
                break
        if not flag:
            break
    if flag:
        if tmp == 0:
            return (1, 0)
        else:
            return (0, 1)

    answer = [0, 0]
    quad = [(x, y), (x + n // 2, y), (x, y + n // 2), (x + n // 2, y + n // 2)]

    for q in quad:
        tmp = recur(n // 2, q[0], q[1], board)
        answer[0] += tmp[0]
        answer[1] += tmp[1]
    return answer


def solution(n, board):
    return recur(n, 0, 0, board)


N = int(sys.stdin.readline().rstrip())
B = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
sol = solution(N, B)
print(sol[0])
print(sol[1])