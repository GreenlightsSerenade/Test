import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = ['' for _ in range(N)]
D = {}
for i in range(N):
    line = sys.stdin.readline().rstrip()
    L[i] = line
    D[line] = i + 1
for i in range(M):
    line = sys.stdin.readline().rstrip()
    if line.isnumeric():
        print(L[int(line) - 1])
    else:
        print(D[line])