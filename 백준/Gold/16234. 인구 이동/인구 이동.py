import sys
from collections import deque


def solution(n, low, high, pop):
    dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    union = [[0 for _ in range(n)] for _ in range(n)]
    totpop = [[0, 0] for _ in range(n * n + 1)]
    for num in range(2001):
        check = 1
        stck = deque()
        for i in range(n * n):
            union[i // n][i % n] = 0
            totpop[i + 1][0], totpop[i + 1][1] = 0, 0
        for i in range(n * n):
            y, x = i // n, i % n
            if union[y][x] != 0:
                continue
            stck.append((y, x))
            union[y][x] = check
            totpop[check][0] += pop[y][x]
            totpop[check][1] += 1
            while stck:
                pos = stck.popleft()
                for j in range(4):
                    new_pos = pos[0] + dxdy[j][0], pos[1] + dxdy[j][1]
                    if (0 <= new_pos[0] < N) and (0 <= new_pos[1] < N) and \
                            (union[new_pos[0]][new_pos[1]] == 0) and \
                            (low <= abs(pop[pos[0]][pos[1]] - pop[new_pos[0]][new_pos[1]]) <= high):
                        stck.append(new_pos)
                        union[new_pos[0]][new_pos[1]] = check
                        totpop[check][0] += pop[new_pos[0]][new_pos[1]]
                        totpop[check][1] += 1
            check += 1
        if check == n * n + 1:
            return num
        for x in range(n * n):
            a, b = totpop[union[x // n][x % n]]
            pop[x // n][x % n] = a // b


N, L, R = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
P = [[] for _ in range(N)]
for i in range(N):
    P[i] = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, L, R, P))