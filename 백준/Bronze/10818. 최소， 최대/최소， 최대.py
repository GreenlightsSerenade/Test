import sys


N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(min(L), max(L))