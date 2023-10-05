import sys
sys.setrecursionlimit(100000)


def find(lst, x):
    if lst[x] == x:
        return x
    else:
        lst[x] = find(lst, lst[x])
        return lst[x]


def solution(n, m):
    lst = [i for i in range(n + 1)]
    for _ in range(m):
        f, a, b = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
        a, b = find(lst, min(a, b)), find(lst, max(a, b))
        if f == 0:
            lst[b] = a
        else:
            if a == b:
                print('YES')
            else:
                print('NO')


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
solution(N, M)