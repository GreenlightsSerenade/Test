import sys


def recur(start, end, lst):
    if end - start == 1:
        return lst[start]
    elif end - start == 2:
        return max(min(lst[start:end]) * 2, max(lst[start:end]))

    mid = (start + end) // 2
    i, j = 0, 0
    mx, h = lst[mid], lst[mid]
    flag = True
    while mid - i > start or mid + j < end - 1:
        if mid - i == start:
            flag = True
        elif mid + j == end - 1:
            flag = False
        elif lst[mid - i - 1] > lst[mid + j + 1]:
            flag = False
        elif lst[mid - i - 1] <= lst[mid + j + 1]:
            flag = True
        if flag:
            j += 1
            h = min(h, lst[mid + j])
        else:
            i += 1
            h = min(h, lst[mid - i])
        mx = max(mx, (j + i + 1) * h)

    return max(recur(start, mid, lst), recur(mid, end, lst), mx)


def solution(n, nums):
    return recur(0, n, nums)


while True:
    L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if L[0] == 0:
        break
    print(solution(L[0], L[1:]))