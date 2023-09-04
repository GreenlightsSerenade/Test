import sys
from collections import deque


def solution(graph):
    cnt = 0
    check = [True for _ in range(101)]
    dq = deque([1])
    check[1] = False
    flag = False
    while dq:
        length = len(dq)
        for _ in range(length):
            now = dq.popleft()
            if len(graph[now]) == 1:
                now = graph[now][0]
            for elem in graph[now]:
                if check[elem]:
                    if elem == 100:
                        flag = True
                        break
                    else:
                        dq.append(elem)
                        check[elem] = False
        cnt += 1
        if flag:
            break
    return cnt

N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
G = {}
for _ in range(N + M):
    a, b = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    G[a] = [b]
for i in range(1, 101):
    if i not in G:
        G[i] = [i + 1, i + 2, i + 3, i + 4, i + 5, i + 6]
print(solution(G))