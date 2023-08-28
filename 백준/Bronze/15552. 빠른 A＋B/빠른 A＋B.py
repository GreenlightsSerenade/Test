import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
    tmp = sys.stdin.readline().rstrip().split(' ')
    print(int(tmp[0]) + int(tmp[1]))