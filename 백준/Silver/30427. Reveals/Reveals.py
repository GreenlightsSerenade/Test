import sys


def solution(house, mkd):
    if 'dongho' in house:
        return 'dongho'
    nmj = sorted(list(house - mkd))
    if len(nmj) == 0:
        return 'swi'
    elif len(nmj) == 1:
        return nmj[0]
    elif 'bumin' in nmj:
        return 'bumin'
    elif 'cake' in nmj:
        return 'cake'
    elif 'lawyer' in nmj:
        return 'lawyer'
    else:
        return nmj[0]


_ = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
H = [sys.stdin.readline().rstrip() for _ in range(N)]
M = int(sys.stdin.readline().rstrip())
K = [sys.stdin.readline().rstrip() for _ in range(M)]
print(solution(set(H), set(K)))