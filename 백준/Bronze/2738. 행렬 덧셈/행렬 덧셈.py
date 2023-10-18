import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L1 = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
L2 = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
for i in range(N):
    for j in range(M):
        print(L1[i][j] + L2[i][j], end='')
        if j == M - 1:
            print()
        else:
            print(' ', end='')