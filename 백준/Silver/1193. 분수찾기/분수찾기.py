import sys

def solution(n):
    if n == 1:
        return '1/1'
    cnt = 1
    m = n - 1
    while m >= cnt:
        m -= cnt
        cnt += 1
    if cnt % 2 == 1:
        return str(cnt - m) + '/' + str(1 + m)
    else:
        return str(1 + m) + '/' + str(cnt - m)

n = int(sys.stdin.readline().strip())
print(solution(n))