import sys
import heapq


def dijkstra(start, end):
    dist = [10**10 for _ in range(200001)]
    hq = []
    heapq.heappush(hq, (0, start))
    dist[start] = 0
    while hq:
        weight, now = heapq.heappop(hq)
        if now > 0 and dist[now - 1] > weight + 1:
            dist[now - 1] = weight + 1
            heapq.heappush(hq, (dist[now - 1], now - 1))
        if now < 100000 and dist[now + 1] > weight + 1:
            dist[now + 1] = weight + 1
            heapq.heappush(hq, (dist[now + 1], now + 1))
        if now < 50001 and dist[2 * now] > weight:
            dist[2 * now] = weight
            heapq.heappush(hq, (dist[2 * now], 2 * now))
    return dist[end]


N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(dijkstra(N, K))