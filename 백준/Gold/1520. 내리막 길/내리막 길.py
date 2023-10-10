import sys


def solution(n, m, map):
    ans = [[-1 for _ in range(m)] for _ in range(n)]
    def DFS(x, y):
        if x == n - 1 and y == m - 1:
            return 1
        if ans[x][y] != -1:
            return ans[x][y]
        ans[x][y] = 0
        d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for dx, dy in d:
            xx, yy = x + dx, y + dy
            if 0 <= xx < n and 0 <= yy < m and map[x][y] > map[xx][yy]:
                ans[x][y] += DFS(xx, yy)
        return ans[x][y]
    return DFS(0, 0)


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, L))