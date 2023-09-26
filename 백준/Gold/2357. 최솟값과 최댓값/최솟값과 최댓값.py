import sys


def st_init(t, nums, start, end, idx, func):
    if start == end:
        t[idx] = nums[start]
        return t[idx]
    else:
        mid = (start + end) // 2
        t[idx] = func(st_init(t, nums, start, mid, idx * 2, func), st_init(t, nums, mid + 1, end, idx * 2 + 1, func))
        return t[idx]


def st_find(t, rge_s, rge_e, start, end, idx, func):
    if rge_s > end or rge_e < start:
        return 0
    if rge_s == start and rge_e == end:
        return t[idx]
    mid = (start + end) // 2
    if rge_e <= mid:
        return st_find(t, rge_s, rge_e, start, mid, idx * 2, func)
    elif rge_s > mid:
        return st_find(t, rge_s, rge_e, mid + 1, end, idx * 2 + 1, func)
    else:
        return func(st_find(t, rge_s, mid, start, mid, idx * 2, func),
                    st_find(t, mid + 1, rge_e, mid + 1, end, idx * 2 + 1, func))


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
mn_tree = [0 for _ in range(N * 4)]
mx_tree = [0 for _ in range(N * 4)]
st_init(mn_tree, L, 0, N - 1, 1, min)
st_init(mx_tree, L, 0, N - 1, 1, max)
for _ in range(M):
    a, b = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    mn = st_find(mn_tree, a, b, 1, N, 1, min)
    mx = st_find(mx_tree, a, b, 1, N, 1, max)
    print(mn, mx)