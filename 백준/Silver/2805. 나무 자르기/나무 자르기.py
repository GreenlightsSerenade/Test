import sys


def solution(n, m, nums):
    start = 0
    end = nums[-1]
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for elem in nums:
            cnt += max(elem - mid, 0)
        if cnt >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, M, sorted(L)))