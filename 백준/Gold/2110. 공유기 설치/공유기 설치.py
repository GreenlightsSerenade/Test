import sys


def solution(n, c, pos, dist):
    if c == 2:
        return pos[-1] - pos[0]
    left = 1
    right = pos[-1] - pos[0]
    while left + 1 < right:
        mid = (left + right) // 2
        tmp, num = 0, 0
        for elem in dist:
            if tmp + elem >= mid:
                tmp, num = 0, num + 1
            else:
                tmp += elem
        if num < c - 1:
            right = mid
        else:
            left = mid
    return left


N, C = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])
D = [L[i + 1] - L[i] for i in range(N - 1)]
print(solution(N, C, L, D))