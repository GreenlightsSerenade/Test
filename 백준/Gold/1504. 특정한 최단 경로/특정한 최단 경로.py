import sys
import heapq

def dijkstra(n, graph, start):
    dist = [10 ** 8 for _ in range(n + 1)]
    hq = []
    dist[start] = 0
    heapq.heappush(hq,  (0, start))

    while hq:
        val, pt = heapq.heappop(hq)
        for k, v in graph[pt].items():
            if dist[pt] + graph[pt][k] < dist[k]:
                dist[k] = dist[pt] + graph[pt][k]
                heapq.heappush(hq, (v, k))
    return dist

def minimize_path(n, graph, v1, v2):
    dist_v1 = dijkstra(n, graph, v1)
    dist_v2 = dijkstra(n, graph, v2)
    if dist_v1[v2] == 10 ** 8:
        return -1
    if dist_v1[1] == 10 ** 8 and dist_v2[1] == 10 ** 8:
        return -1
    if dist_v1[n] == 10 ** 8 and dist_v2[n] == 10 ** 8:
        return -1
    return dist_v1[v2] + min(dist_v1[1] + dist_v2[n], dist_v2[1] + dist_v1[n])

n, e = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
graph = [dict() for _ in range(n + 1)]
for _ in range(e):
    tmp = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph[tmp[0]][tmp[1]] = tmp[2]
    graph[tmp[1]][tmp[0]] = tmp[2]
v1, v2 = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))

print(minimize_path(n, graph, v1, v2))