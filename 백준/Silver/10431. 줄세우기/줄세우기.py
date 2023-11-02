import sys


def solution(nums):
    ans = 0
    temp = [0 for _ in range(20)]
    temp[0] = nums[0]
    for i in range(1, 20):
        temp[i] = nums[i]
        for j in range(i):
            if temp[j] > temp[i]:
                ans += (i - j)
                for k in range(i - j):
                    temp[i - k], temp[i - k - 1] = temp[i - k - 1], temp[i - k]
                break
    return ans


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    T, *P = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(T, solution(P))