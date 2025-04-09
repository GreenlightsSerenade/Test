import sys
from collections import deque


def solution(n, k, conv):
    ans = 1
    cnt = 0
    robots = deque([False for _ in range(n * 2)])
    while ans:
        conv.rotate(1)
        robots.rotate(1)
        if robots[n - 1]:
            robots[n - 1] = False
        if robots[n - 2]:
            if conv[n - 1] > 0:
                conv[n - 1] -= 1
                if conv[n - 1] == 0:
                    cnt += 1
                robots[n - 2] = False
        for i in range(1, n - 1):
            if robots[n - 2 - i] and (not robots[n - 1 - i]) and conv[n - 1 - i] > 0:
                robots[n - 1 - i] = True
                robots[n - 2 - i] = False
                conv[n - 1 - i] -= 1
                if conv[n - 1 - i] == 0:
                    cnt += 1
        if conv[0] > 0:
            robots[0] = True
            conv[0] -= 1
            if conv[0] == 0:
                cnt += 1
        if cnt >= k:
            return ans
        ans += 1


N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = deque(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, K, L))