import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = ['0' for _ in range(N)]
for _ in range(M):
    t = sys.stdin.readline().rstrip().split(' ')
    for x in range(int(t[0]), int(t[1]) + 1):
        L[x - 1] = t[2]
print(' '.join(L))