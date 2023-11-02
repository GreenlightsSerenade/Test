import sys


def solution(pos):
    mn, mx = pos[0][0], pos[0][1]
    ans = 0
    for x, y in pos[1:]:
        if x > mx:
            ans += mx - mn
            mn, mx = x, y
        elif x <= mx < y:
            mx = y
    return ans + mx - mn


N = int(sys.stdin.readline().rstrip())
L = [sorted(tuple(map(int, sys.stdin.readline().rstrip().split(' ')))) for _ in range(N)]
print(solution(sorted(L)))