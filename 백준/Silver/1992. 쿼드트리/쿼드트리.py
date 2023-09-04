import sys


def recur(n, x, y, board):
    if n == 1:
        sys.stdout.write(board[y][x])
        return None

    tmp = board[y][x]
    flag = True
    for i in range(y, y + n):
        for j in range(x, x + n):
            if tmp != board[i][j]:
                flag = False
                break
        if not flag:
            break
    if flag:
        sys.stdout.write(tmp)
        return None

    quad = [(x, y), (x + n // 2, y), (x, y + n // 2), (x + n // 2, y + n // 2)]

    sys.stdout.write('(')
    for q in quad:
        recur(n // 2, q[0], q[1], board)
    sys.stdout.write(')')
    return None


def solution(n, board):
    recur(n, 0, 0, board)


N = int(sys.stdin.readline().rstrip())
B = [sys.stdin.readline().rstrip() for _ in range(N)]
solution(N, B)