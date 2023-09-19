import sys


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    print(line[0] + line[-1])