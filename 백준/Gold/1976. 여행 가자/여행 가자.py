import sys


def solution(n, m, graph, route):
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        check[i][i] = 1
        tmp = []
        for j in range(n):
            if graph[i][j] == 1:
                tmp.append(j)
        while tmp:
            now = tmp.pop()
            check[i][now] = 1
            for k in range(n):
                if check[i][k] == 0 and graph[now][k] == 1:
                    tmp.append(k)
    for i in range(m - 1):
        if check[route[i] - 1][route[i + 1] - 1] == 0:
            return 'NO'
    return 'YES'


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
G = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
R = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, M, G, R))