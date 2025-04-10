import sys
from collections import deque


def solution(n, k, ground, trees):
    dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    enermap = [[5 for _ in range(n)] for _ in range(n)]
    ans = 0
    for _ in range(k):
        for i in range(n):
            for j in range(n):
                tmp = deque()
                r = 0
                for age in trees[i][j]:
                    if age <= enermap[i][j]:
                        enermap[i][j] -= age
                        tmp.append(age + 1)
                    else:
                        r += (age // 2)
                trees[i][j] = tmp
                enermap[i][j] += r
        for i in range(n):
            for j in range(n):
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for dx, dy in dxdy:
                            new_x, new_y = i + dx, j + dy
                            if (0 <= new_x < n) and (0 <= new_y < n):
                                trees[new_x][new_y].appendleft(1)
                enermap[i][j] += ground[i][j]
    for r in range(n):
        for c in range(n):
            ans += len(trees[r][c])

    return ans


N, M, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
T = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    T[x - 1][y - 1].append(z)
print(solution(N, K, G, T))