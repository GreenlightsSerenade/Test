import sys

def solution(n,):
    if n == 1:
        return 9
    DP = [[0 for _ in range(10)] for _ in range(n)]
    for i in range(1, 10):
        DP[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                DP[i][j] = DP[i - 1][j + 1]
            elif j == 9:
                DP[i][j] = DP[i - 1][j - 1]
            else:
                DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 1000000000

    return sum(DP[-1]) % 1000000000

n = int(sys.stdin.readline().rstrip())

print(solution(n))