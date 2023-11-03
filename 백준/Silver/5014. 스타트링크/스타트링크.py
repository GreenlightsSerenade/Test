import sys


def solution(f, s, g, u, d):
    graph = {}
    check = [True for _ in range(f + 1)]
    for i in range(1, f + 1):
        graph[i] = (i - d, i + u)
    stck = [s]
    check[s] = False
    ans = 0
    while stck:
        length = len(stck)
        for _ in range(length):
            now = stck.pop(0)
            if now == g:
                return ans
            if graph[now][0] > 0 and check[graph[now][0]]:
                stck.append(graph[now][0])
                check[graph[now][0]] = False
            if graph[now][1] <= f and check[graph[now][1]]:
                stck.append(graph[now][1])
                check[graph[now][1]] = False
        ans += 1
    return 'use the stairs'


F, S, G, U, D = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(F, S, G, U, D))