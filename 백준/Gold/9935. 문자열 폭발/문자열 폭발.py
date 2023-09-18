import sys


def solution(line, bomb):
    stck = []
    bl = len(bomb)
    for c in line:
        stck.append(c)
        i, cnt = 0, 0
        while len(stck) >= bl > cnt and stck[-1 - i] == bomb[-1 - i]:
            i += 1
            cnt += 1
        if cnt == bl:
            for _ in range(bl):
                stck.pop()
    if len(stck) == 0:
        return 'FRULA'
    return ''.join(stck)


line1 = sys.stdin.readline().rstrip()
line2 = sys.stdin.readline().rstrip()
print(solution(line1, line2))