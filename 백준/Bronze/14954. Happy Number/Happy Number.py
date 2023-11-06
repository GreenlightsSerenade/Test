import sys


def solution(n):
    while n >= 10:
        tmp1, tmp2 = 0, n
        while tmp2 > 0:
            tmp1 += (tmp2 % 10) ** 2
            tmp2 //= 10
        n = tmp1
    if n == 1 or n == 7:
        return 'HAPPY'
    else:
        return 'UNHAPPY'


N = int(sys.stdin.readline().rstrip())
print(solution(N))