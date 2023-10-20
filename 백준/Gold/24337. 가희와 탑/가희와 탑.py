import sys


def solution(n, a, b):
    c = n - a - b
    if c < -1:
        return '-1'
    elif c >= 0:
        ans = [1 for _ in range(c + 1)]
    else:
        ans = []

    if a > b:
        ans += [i + 1 for i in range(a)] + [i for i in range(b - 1, 0, -1)]
    else:
        if a == 1:
            ans = [b] + ans + [i for i in range(b - 1, 0, -1)]
        else:
            ans += [i + 1 for i in range(a - 1)] + [i for i in range(b, 0, -1)]
    return ' '.join(map(str, ans))


N, A, B = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, A, B))