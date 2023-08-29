import sys

n = int(sys.stdin.readline().rstrip())

d = dict()
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(' ')
    if a == 'ChongChong' or b == 'ChongChong':
        d[a], d[b] = 1, 1
    elif a not in d and b not in d:
        d[a], d[b] = 0, 0
    elif a not in d and b in d:
        d[a] = d[b]
    elif a in d and b not in d:
        d[b] = d[a]
    else:
        if d[a] > d[b]:
            d[b] = 1
        elif d[b] > d[a]:
            d[a] = 1
            
print(sum(d.values()))