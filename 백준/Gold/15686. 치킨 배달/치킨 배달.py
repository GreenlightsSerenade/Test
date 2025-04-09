import sys
from collections import deque


def solution(n, m, chick):
    house = []
    ch = []
    for i in range(n * n):
        y, x = i // n, i % n
        if chick[y][x] == 1:
            house.append((y, x))
        elif chick[y][x] == 2:
            ch.append((y, x))
    lench = len(ch)
    per_house = []

    def comb(per_lim, new_arr, c):
        if len(new_arr) == per_lim:
            per_house.append(new_arr)
            return
        for p in range(c, lench):
            comb(per_lim, new_arr + [ch[p]], p + 1)

    comb(m, [], 0)
    ans = 8909999903
    for pers in per_house:
        cal = 0
        for h in house:
            ret = 10000000
            for per in pers:
                ret = min(ret, abs(h[0] - per[0]) + abs(h[1] - per[1]))
            cal += ret
        ans = min(ans, cal)
    return ans


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
maping = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, maping))