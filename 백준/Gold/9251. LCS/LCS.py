import sys


def solution(x, y):
    lx, ly = len(x), len(y)
    DP = [[0 for _ in range(lx + 1)] for _ in range(ly + 1)]
    for i in range(1, ly + 1):
        for j in range(1, lx + 1):
            if y[i - 1] == x[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
    return DP[-1][-1]


L1 = sys.stdin.readline().rstrip()
L2 = sys.stdin.readline().rstrip()
print(solution(L1, L2))