import sys

def solution(lst, n, s):
    p1, p2 = 0, 0
    mn = n + 1
    now_sum = lst[0]

    while p2 < n:
        if now_sum >= s:
            if p1 == p2:
                return 1
            mn = min(p2 - p1 + 1, mn)
            now_sum -= lst[p1]
            p1 += 1
        else:
            p2 += 1
            if p2 < n:
                now_sum += lst[p2]
    if mn == n + 1:
        return 0
    return mn

n, s = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(lst, n, s))