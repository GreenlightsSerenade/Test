import sys
from collections import deque


def solution(n, m, energy, ground, s, desti):
    dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    start = (s[0] - 1, s[1] - 1)

    def findroute(s_pos, ener, dest=None):
        visited = [[-1 for _ in range(n)] for _ in range(n)]
        stck = deque([s_pos])
        cnt = 0
        visited[s_pos[0]][s_pos[1]] = cnt
        flag = False
        ret = [(n + 1, n + 1), -1, -1]
        while stck:
            #print(stck)
            l = len(stck)
            cnt += 1
            for _ in range(l):
                elem = stck.popleft()
                if dest is None:
                    if ground[elem[0]][elem[1]] > 1:
                        flag = True
                        if elem[0] < ret[0][0] or (elem[0] == ret[0][0] and elem[1] < ret[0][1]):
                            ret = [elem, visited[elem[0]][elem[1]], ener]
                else:
                    if elem == dest:
                        flag = True
                        if elem[0] < ret[0][0] or (elem[0] == ret[0][0] and elem[1] < elem[0][1]):
                            ret = [elem, visited[elem[0]][elem[1]], ener]
                for i in range(4):
                    new_x, new_y = elem[0] + dxdy[i][0], elem[1] + dxdy[i][1]
                    if ((0 <= new_x < n and 0 <= new_y < n) and (ground[new_x][new_y] != 1)
                            and (visited[new_x][new_y] == -1)):
                        stck.append((new_x, new_y))
                        visited[new_x][new_y] = cnt
            if flag:
                return ret
            ener -= 1
            if ener < 0:
                return ret
        return ret
    for _ in range(m):
        value = findroute(start, energy)
        if value[2] == -1:
            return -1
        start, energy = value[0], value[2]
        #print('start: ', value)
        value2 = findroute(start, energy, desti[value[0]])
        ground[start[0]][start[1]] = 0
        if value2[2] == -1:
            return -1
        start, energy = value2[0], value2[1] * 2 + value2[2]
        #print('end: ', value2)
    return energy


N, M, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
S = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
D = {}
for i in range(M):
    x, y, z, w = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    G[x - 1][y - 1] = i + 2
    D[(x - 1, y - 1)] = (z - 1, w - 1)
print(solution(N, M, K, G, S, D))
# tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
# list(map(int, sys.stdin.readline().rstrip().split(' ')))
# N = int(sys.stdin.readline().rstrip())
# line = sys.stdin.readline().rstrip()
