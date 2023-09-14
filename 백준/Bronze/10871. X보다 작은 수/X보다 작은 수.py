import sys


N, X = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
R = []
for elem in L:
    if elem < X:
        R.append(str(elem))
print(' '.join(R))