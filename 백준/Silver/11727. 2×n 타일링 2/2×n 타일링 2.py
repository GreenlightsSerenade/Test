import sys


def solution(n):
    if n == 1:
        return 1
    DP = [0 for _ in range(n + 1)]
    DP[1] = 1
    DP[2] = 3
    for i in range(3, n + 1):
        DP[i] = (2 * DP[i - 2] + DP[i - 1]) % 10007
    return DP[n]


N = int(sys.stdin.readline().rstrip())
print(solution(N))