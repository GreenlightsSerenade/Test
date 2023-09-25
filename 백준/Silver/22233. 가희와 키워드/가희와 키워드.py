import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
S = set([sys.stdin.readline().rstrip() for _ in range(N)])
for _ in range(M):
    lines = sys.stdin.readline().rstrip().split(',')
    for line in lines:
        if line in S:
            S.remove(line)
    print(len(S))