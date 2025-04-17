import sys
from collections import deque, defaultdict
from itertools import combinations
import heapq

def solution(r, c, l):
    dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    tmp = {'#': -1, '.': 0, 'F': -2, 'J': 2}
    graph = [[tmp[l[i][j]] for j in range(c)] for i in range(r)]
    visited = [[False if graph[i][j] >= 0 else True for j in range(c)] for i in range(r)]
    pos_j, pos_f = None, None
    stck_f = deque()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 2:
                pos_j = (i, j)
                visited[i][j] = True
            elif graph[i][j] == -2:
                stck_f.append((i, j))
    stck_j = deque([pos_j])
    cnt = 0
    while stck_j:
        lj, lf = len(stck_j), len(stck_f)
        for _ in range(lf):
            px, py = stck_f.popleft()
            for dx, dy in dxdy:
                npx, npy = px + dx, py + dy
                if 0 <= npx < r and 0 <= npy < c and (not visited[npx][npy]):
                    visited[npx][npy] = True
                    stck_f.append((npx, npy))
        for _ in range(lj):
            jx, jy = stck_j.popleft()
            for dx, dy in dxdy:
                njx, njy = jx + dx, jy + dy
                if not (0 <= njx < r and 0 <= njy < c):
                    return cnt + 1
                elif not visited[njx][njy]:
                    stck_j.append((njx, njy))
                    visited[njx][njy] = True
        cnt += 1
    return 'IMPOSSIBLE'


R, C = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
print(solution(R, C, L))