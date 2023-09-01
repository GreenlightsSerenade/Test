import sys


def solution(n, nums):
    cnt1, cnt2 = 0, 0
    tmp1 = [0 for _ in range(n)]
    tmp2 = [0 for _ in range(n)]
    DP = [0 for _ in range(n)]
    tmp1[0], tmp2[0] = nums[0], nums[n - 1]
    for i in range(1, n):
        x, y = 0, 0
        while nums[i] <= tmp1[cnt1 - x] and x <= cnt1:
            x += 1
        while nums[n - i - 1] <= tmp2[cnt2 - y] and y <= cnt2:
            y += 1
        tmp1[cnt1 - x + 1] = nums[i]
        tmp2[cnt2 - y + 1] = nums[n - i - 1]
        if x == 0:
            cnt1 += 1
        if y == 0:
            cnt2 += 1
        DP[i] += cnt1
        DP[n - i - 1] += cnt2
    return max(DP) + 1


N = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, lst))