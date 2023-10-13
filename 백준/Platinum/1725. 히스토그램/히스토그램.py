import sys


def solution(n, nums):
    stck = [0]
    ans = -1
    for i, elem in enumerate(nums):
        while stck and elem < nums[stck[-1]]:
            pos = stck.pop()
            v = i if not stck else i - stck[-1] - 1
            ans = max(nums[pos] * v, ans)
        stck.append(i)
    while stck:
        pos = stck.pop()
        v = n if not stck else n - stck[-1] - 1
        ans = max(nums[pos] * v, ans)
    return ans


N = int(sys.stdin.readline().rstrip())
L = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
print(solution(N, L))
