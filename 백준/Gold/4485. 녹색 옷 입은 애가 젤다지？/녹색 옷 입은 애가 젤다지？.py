import sys
from collections import deque, defaultdict
import heapq


def solution(n, zelda):
    l_list = defaultdict(list)
    dxdy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    dist = [[zelda[0][0] if i == 0 and j == 0 else 999999 for i in range(n)] for j in range(n)]
    h = [(zelda[0][0], (0, 0))]
    visited = [False for _ in range(n * n)]
    for i in range(n):
        for j in range(n):
            for dx, dy in dxdy:
                if 0 <= i + dx < n and 0 <= j + dy < n:
                    l_list[(i, j)].append((zelda[i + dx][j + dy], (i + dx, j + dy)))
    while h:
        now_val, pos = heapq.heappop(h)
        visited[n] = True
        for value, (px, py) in l_list[pos]:
            newdat = dist[pos[0]][pos[1]] + value
            if newdat < dist[px][py]:
                dist[px][py] = newdat
                heapq.heappush(h, (newdat, (px, py)))
    return dist[-1][-1]

c = 1
while True:
    N = int(sys.stdin.readline().rstrip())
    if N == 0:
        break
    L = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
    print(f'Problem {c}: {solution(N, L)}')
    c += 1