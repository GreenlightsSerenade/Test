import sys


def knapsack(n, k, objects):
    DP = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    objects.sort()
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if objects[i - 1][0] <= j:
                DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - objects[i - 1][0]] + objects[i - 1][1])
            else:
                DP[i][j] = DP[i - 1][j]
    return DP[-1][-1]


N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
OBJ = []
for _ in range(N):
    OBJ.append(tuple(map(int, sys.stdin.readline().rstrip().split(' '))))
print(knapsack(N, K, OBJ))