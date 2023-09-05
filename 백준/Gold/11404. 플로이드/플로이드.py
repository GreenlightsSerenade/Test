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
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if dist[i][j] == 10 ** 9:
                sys.stdout.write('0')
            else:
                sys.stdout.write(str(dist[i][j]))
            if j == num:
                sys.stdout.write('\n')
            else:
                sys.stdout.write(' ')


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
G = [[10 ** 9 if i != j else 0 for j in range(N + 1)] for i in range(N + 1)]
for _ in range(M):
    A, B, C = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    G[A][B] = min(G[A][B], C)
floydwarshall(N, G)