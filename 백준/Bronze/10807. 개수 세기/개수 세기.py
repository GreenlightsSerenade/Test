import sys


N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
K = int(sys.stdin.readline().rstrip())
ans = 0
for e in L:
    if K == e:
        ans += 1
print(ans)