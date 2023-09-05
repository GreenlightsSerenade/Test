import sys
from collections import deque


def solution(n, m, graph):
    if n == 1 and m == 1:
        return 1
    cnt = 1
    check = [[[True, True] for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dq = deque([(0, 0, 0)])
    check[0][0] = [False, False]
    flag = False
    while dq:
        length = len(dq)
        for _ in range(length):
            now = dq.popleft()
            for elem in d:
                dx, dy = now[0] + elem[0], now[1] + elem[1]
                if 0 <= dx < n and 0 <= dy < m:
                    if dx == n - 1 and dy == m - 1:
                        flag = True
                        break
                    elif graph[dx][dy] == '0' and check[dx][dy][now[2]]:
                        dq.append((dx, dy, now[2]))
                        check[dx][dy][now[2]] = False
                    elif graph[dx][dy] == '1' and now[2] == 0 and check[dx][dy][1]:
                        dq.append((dx, dy, 1))
                        check[dx][dy][1] = False
        cnt += 1
        if flag:
            break
    if not flag:
        return -1
    return cnt


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
print(solution(N, M, G))