import sys


def floydwarshall(num, graph):
    dist = [[10 ** 9 if i != j else 0 for j in range(num + 1)] for i in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            dist[i][j] = graph[i][j]
    for k in range(1, num + 1):
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 10 ** 9
    for i in range(1, num):
        for j in range(i + 1, num + 1):
            ans = min(ans, dist[i][j] + dist[j][i])
    if ans == 10 ** 9:
        return -1
    return ans


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = [[10 ** 9 if i != j else 0 for j in range(N + 1)] for i in range(N + 1)]
for _ in range(M):
    A, B, C = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    G[A][B] = C
print(floydwarshall(N, G))