import sys


def solution(n, d, nums):
    answer = 0
    sums = [0 for _ in range(n)]
    rems = [0 for _ in range(d)]
    sums[0] = nums[0] % d
    rems[sums[0]] += 1
    for i in range(1, n):
        sums[i] = (sums[i - 1] + nums[i]) % d
        rems[sums[i]] += 1
    for i in range(d):
        if rems[i] != 0:
            answer += rems[i] * (rems[i] - 1) // 2
    return answer + rems[0]


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
AN = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, M, AN))