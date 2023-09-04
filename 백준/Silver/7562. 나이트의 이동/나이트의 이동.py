import sys
from collections import deque


def solution(n, start, end):
    if start == end:
        return 0
    check = [[True for _ in range(n)] for _ in range(n)]
    check[start[0]][start[1]] = False
    dq = deque([start])
    d = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    flag = False
    cnt = 0

    while dq:
        length = len(dq)
        for _ in range(length):
            now = dq.popleft()
            for elem in d:
                dx, dy = now[0] + elem[0], now[1] + elem[1]
                if 0 <= dx < n and 0 <= dy < n:
                    if dx == end[0] and dy == end[1]:
                        flag = True
                        break
                    elif check[dx][dy]:
                        dq.append((dx, dy))
                        check[dx][dy] = False
        cnt += 1
        if flag:
            break
    return cnt

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    L = int(sys.stdin.readline().rstrip())
    ST = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    ED = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(solution(L, ST, ED))