import sys


def recur(n, x, y, board):
    if n == 1:
        if board[y][x] == -1:
            return (1, 0, 0)
        elif board[y][x] == 0:
            return (0, 1, 0)
        else:
            return (0, 0, 1)

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
        if tmp == -1:
            return (1, 0, 0)
        elif tmp == 0:
            return (0, 1, 0)
        else:
            return (0, 0, 1)

    nine = [(x, y), (x + n // 3, y), (x + (n // 3) * 2, y),
            (x, y + n // 3), (x + n // 3, y + n // 3), (x + (n // 3) * 2, y + n // 3),
            (x, y + 2 * (n // 3)), (x + n // 3, y + 2 * (n // 3)), (x + (n // 3) * 2, y + 2 * (n // 3))]

    answer = [0, 0, 0]
    for nn in nine:
        tmp = recur(n // 3, nn[0], nn[1], board)
        answer[0] += tmp[0]
        answer[1] += tmp[1]
        answer[2] += tmp[2]
    return answer


def solution(n, board):
    return recur(n, 0, 0, board)


N = int(sys.stdin.readline().rstrip())
B = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
sol = solution(N, B)
for i in range(3):
    print(sol[i])