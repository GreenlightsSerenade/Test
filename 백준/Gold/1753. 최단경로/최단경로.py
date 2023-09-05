import sys
import heapq


def dijkstra(v, graph, start):
    dist = [10**10 for _ in range(v + 1)]
    hq = []
    heapq.heappush(hq, (0, start))
    dist[start] = 0
    while hq:
        weight, now = heapq.heappop(hq)
        if now in graph:
            for w, p in graph[now]:
                if dist[p] > weight + w:
                    dist[p] = weight + w
                    heapq.heappush(hq, (dist[p], p))
    for i in range(1, v + 1):
        if dist[i] == 10**10:
            print('INF')
        else:
            print(dist[i])
    return None


V, E = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
ST = int(sys.stdin.readline().rstrip())
G = {}
for _ in range(E):
    u, v, w = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    if u in G:
        G[u].append((w, v))
    else:
        G[u] = [(w, v)]
dijkstra(V, G, ST)