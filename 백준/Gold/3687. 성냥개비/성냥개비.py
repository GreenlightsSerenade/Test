import sys


def solution(n):
    if n == 2:
        return ['1', '1']
    elif n == 3:
        return ['7', '7']

    mn = 0
    tmp = [-1, -1, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20, 28, 68, 88, 108, 188, 200, 208, 288, 688, 888]
    if n <= 21:
        mn = tmp[n]
    else:
        q = (n + 6) // 7 - 3
        mn += tmp[n - q * 7] * (10 ** q)
        while q > 0:
            mn += 8 * (10 ** (q - 1))
            q -= 1

    mx, m, k = 0, n, 1
    while m > 3:
        if m == 4:
            mx += 10 * k + k
        elif m == 5:
            mx += 10 * 7 * k + k
        else:
            mx += k
        k *= 10
        m -= 2
    return [str(mn), str(mx)]


N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    M = int(sys.stdin.readline().rstrip())
    print(' '.join(solution(M)))