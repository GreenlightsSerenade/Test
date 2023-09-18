import sys


def solution(n, nums):
    if n == 1 or n == 2:
        return n - 1
    stck = []
    ans = 0
    for num in nums:
        if not stck:
            stck.append([num, 1])
        else:
            if stck[-1][0] > num:
                stck.append([num, 1])
                ans += 1
            else:
                cnt = 0
                while stck and (stck[-1][0] == num or stck[-1][0] < num):
                    elem, x = stck.pop()
                    ans += x
                    if elem == num:
                        cnt = x
                if stck and stck[-1][0] > num:
                    ans += 1
                stck.append([num, cnt + 1])
    return ans


N = int(sys.stdin.readline().rstrip())
L = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
print(solution(N, L))