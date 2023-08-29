import sys

n, m = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))

d = dict()
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if len(line) < m:
        pass
    else:
        if line in d:
            d[line] += 1
        else:
            d[line] = 1

srt_d = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for elem in srt_d:
    sys.stdout.write(elem[0] + '\n')
