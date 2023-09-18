import sys
from collections import defaultdict, deque


def solution(n, tree):
    parents = [0 for _ in range(n + 1)]
    now = deque([])
    parents[1] = -1
    for elem in tree[1]:
        now.append((elem, 1))

    while now:
        length = len(now)
        for _ in range(length):
            e = now.popleft()
            parents[e[0]] = e[1]
            for elem in tree[e[0]]:
                if parents[elem] == 0:
                    now.append((elem, e[0]))

    for elem in parents[2:]:
        print(elem)


N = int(sys.stdin.readline().rstrip())
D = defaultdict(list)
for _ in range(N - 1):
    x, y = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    D[x].append(y)
    D[y].append(x)
solution(N, D)