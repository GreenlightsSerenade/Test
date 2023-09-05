import sys
import heapq


def dijkstra(num, graph, start):
    dist = [10 ** 9 for _ in range(num + 1)]
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        weight, now = heapq.heappop(hq)
        for w, p in graph[now]:
            if dist[p] > weight + w:
                dist[p] = weight + w
                heapq.heappush(hq, (dist[p], p))
    return dist


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m, t = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    s, g, h = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    GR = {}
    P = 0
    for i in range(n):
        GR[i + 1] = []
    for _ in range(m):
        a, b, d = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
        if (a == g and b == h) or (a == h and b == g):
            P = d
        GR[a].append((d, b))
        GR[b].append((d, a))
    D = sorted([int(sys.stdin.readline().rstrip()) for _ in range(t)])
    ss, gg, hh = dijkstra(n, GR, s), dijkstra(n, GR, g), dijkstra(n, GR, h)
    ans = []
    for elem in D:
        if ss[elem] == gg[s] + hh[elem] + P or ss[elem] == gg[elem] + hh[s] + P:
            ans.append(str(elem))
    print(' '.join(ans))