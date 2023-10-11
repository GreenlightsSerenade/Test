import sys


def solution(n, gs, m, cks):
    s = sum(gs)
    DP = [[0 for _ in range(2 * s + 10)] for _ in range(n)]
    DP[0][0] = 1
    DP[0][-gs[0]] = 1
    DP[0][gs[0]] = 1
    for i in range(1, n):
        for j in range(s + 1):
            if DP[i - 1][j] == 1:
                DP[i][j - gs[i]] = 1
                DP[i][j] = 1
                if j + gs[i] <= s:
                    DP[i][j + gs[i]] = 1
        for j in range(s + 1):
            if DP[i - 1][-j] == 1:
                DP[i][-j - gs[i]] = 1
                DP[i][-j] = 1
                if gs[i] - j >= -s:
                    DP[i][gs[i] - j] = 1
    mm = []
    for elem in cks:
        if elem > s or DP[-1][elem] == 0:
            mm.append('N')
        else:
            mm.append('Y')
    return ' '.join(mm)


N = int(sys.stdin.readline().rstrip())
L1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())
L2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, sorted(L1), M, L2))