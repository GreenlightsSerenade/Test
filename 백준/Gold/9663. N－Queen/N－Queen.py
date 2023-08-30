import sys

def n_queen_check(board, n, pos):
    for i in range(n):
        if board[i] == pos:
            return False
        if i - board[i] == n - pos:
            return False
        if i + board[i] == n + pos:
            return False
    return True

def n_queen(board, cnt, stp, ret):
    if cnt == stp:
        return ret + 1
    for i in range(n):
        if cnt == 0 or n_queen_check(board, cnt, i):
            board[cnt] = i
            ret = n_queen(board, cnt + 1, stp, ret)
    return ret

def solution(n):
    board = [-1 for _ in range(n)]
    return n_queen(board, 0, n, 0)

n = int(sys.stdin.readline().rstrip())
print(solution(n))