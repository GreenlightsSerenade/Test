import sys

def solution(lst, n):
    start, end = 0, n - 1
    mn = int(2e9 + 1)
    ret1, ret2, tmp = None, None, None
    while start < end:
        tmp = lst[start] + lst[end]
        if abs(tmp) < mn:
            ret1, ret2, mn = lst[start], lst[end], abs(tmp)
        elif tmp < 0:
            start += 1
        else:
            end -= 1
    return ret1, ret2

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
sol = solution(sorted(lst), n)
print(sol[0], sol[1])