import sys

def solution(n):
    if n == 1:
        return 1
    else:
        tmp = (n - 2) // 6
        cnt = 1
        ret = 1
        while tmp >= 0:
            tmp -= cnt
            cnt += 1
            ret += 1
        return ret

n = int(sys.stdin.readline().strip())
print(solution(n))
