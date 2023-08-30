import sys

def calcul(n, graph, flag, mn):
    ret = 0
    for i in range(n):
        for j in range(i + 1, n):
            if flag[i] and flag[j]:
                ret += (graph[i][j] + graph[j][i])
            elif not (flag[i] or flag[j]):
                ret -= (graph[i][j] + graph[j][i])
    return min(mn, abs(ret))

def recur(n, cnt, stp, graph, flag, mn, go):
    if cnt == stp:
        return calcul(n, graph, flag, mn)
    for i in range(go, n):
        if not flag[i]:
            flag[i] = True
            mn = recur(n, cnt + 1, stp, graph, flag, mn, i + 1)
            flag[i] = False
    return mn

def solution(n, graph):
    flag = [False for _ in range(n)]
    return recur(n, 0, n // 2, graph, flag, int(1e9), 0)

n = int(sys.stdin.readline().rstrip())
graph = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(solution(n, graph))