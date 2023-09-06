import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
MT1 = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
_, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
MT2 = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(M)]
MT3 = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        for x in range(M):
            MT3[i][j] += MT1[i][x] * MT2[x][j]
for i in range(N):
    for j in range(K):
        sys.stdout.write(str(MT3[i][j]))
        if j == K - 1:
            sys.stdout.write('\n')
        else:
            sys.stdout.write(' ')