import sys


def solution(n, a, b, k):
    ans = 0
    for i in range(n):
        if k[i] < 10:
            ans += (a[i] - (b[i] * k[i]) // 10)
        else:
            ans += ((a[i] * k[i]) // 10 - b[i])
    return ans


N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
B = list(map(int, sys.stdin.readline().rstrip().split(' ')))
K = list(map(int, list(map(lambda x: x[:-2] + x[-1:], sys.stdin.readline().rstrip().split(' ')))))

print(solution(N, A, B, K))