import sys


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
x = {sys.stdin.readline().rstrip() for _ in range(N)}
y = {sys.stdin.readline().rstrip() for _ in range(M)}
z = sorted(list(x & y))
w = len(z)
print(w)
for i in range(w):
    print(z[i])