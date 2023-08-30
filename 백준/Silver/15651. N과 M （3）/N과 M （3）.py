import sys

def recur(arr, cnt, length, stp, ret):
    if cnt == stp:
        print(' '.join(ret))
        return
    for i in range(length):
        ret[cnt] = str(arr[i])
        recur(arr, cnt + 1, length, stp, ret)

def solution(n, m):
    arr = list(range(1, n + 1))
    ret = ["" for _ in range(m)]
    recur(arr, 0, n, m, ret)


n, m = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
solution(n, m)