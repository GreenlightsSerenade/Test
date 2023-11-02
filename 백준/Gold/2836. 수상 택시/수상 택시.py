import sys


def solution(pos):
    if len(pos) == 0:
        return 0
    mn, mx = pos[0][0], pos[0][1]
    ans = 0
    for x, y in pos[1:]:
        if x > mx:
            ans += mx - mn
            mn, mx = x, y
        elif x <= mx < y:
            mx = y
    return ans + mx - mn


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = []
for _ in range(N):
    a, b = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    if a > b:
        L.append((b, a))
print(M + 2 * solution(sorted(L)))