import sys
from collections import deque


def solution(n, start, graph):
    check = [0 for _ in range(n)]
    check[start - 1] = 1
    cnt = 2
    dq = deque([start])

    while dq:
        now = dq.popleft()
        if now not in graph:
            continue
        for elem in sorted(graph[now], reverse=True):
            if check[elem - 1] == 0:
                check[elem - 1] = cnt
                cnt += 1
                dq.append(elem)
    for elem in check:
        print(elem)


N, M, R = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = {}
for _ in range(M):
    u, v = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    if u in G:
        G[u].append(v)
    else:
        G[u] = [v]
    if v in G:
        G[v].append(u)
    else:
        G[v] = [u]
solution(N, R, G)