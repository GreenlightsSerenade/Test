import sys

n = int(sys.stdin.readline().rstrip())

s = set()
ret = 0
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if line != 'ENTER':
        s.add(line)
    else:
        ret += len(s)
        s = set()
ret += len(s)
print(ret)