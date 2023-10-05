import sys


def solution(n, nums):
    DP = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    sums = [nums[0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        sums[i] = nums[i - 1] + sums[i - 1]

    for i in range(1, n + 1):
        for j in range(n + 1 - i):
            DP[j][i + j] = 10 ** 10
            for k in range(j, i + j):
                DP[j][i + j] = min(DP[j][i + j], DP[j][k] + DP[k + 1][i + j] + sums[i + j] - sums[j - 1])
    return DP[1][-1]


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(solution(K, L))