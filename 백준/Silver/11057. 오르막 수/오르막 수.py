import sys


def solution(n):
    if n == 1:
        return 10
    DP = [[0 for _ in range(10)] for _ in range(n + 1)]
    DP[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(2, n + 1):
        DP[i][0] = 1
        for j in range(1, 10):
            DP[i][j] = (DP[i][j - 1] + DP[i - 1][j]) % 10007
    return sum(DP[n]) % 10007


N = int(sys.stdin.readline().rstrip())
print(solution(N))