import sys


def st_init(t, nums, start, end, idx):
    if start == end:
        t[idx] = nums[start]
        return t[idx]
    else:
        mid = (start + end) // 2
        t[idx] = (st_init(t, nums, start, mid, idx * 2) * st_init(t, nums, mid + 1, end, idx * 2 + 1)) % 1000000007
        return t[idx]


def st_update(t, pos, data, start, end, idx):
    if start == end:
        t[idx] = data
        loopy = idx // 2
        while loopy > 0:
            t[loopy] = (t[loopy * 2] * t[loopy * 2 + 1]) % 1000000007
            loopy //= 2
        return
    mid = (start + end) // 2
    if pos <= mid:
        st_update(t, pos, data, start, mid, idx * 2)
    else:
        st_update(t, pos, data, mid + 1, end, idx * 2 + 1)


def st_product(t, rge_s, rge_e, start, end, idx):
    if rge_s > end or rge_e < start:
        return 0
    if rge_s == start and rge_e == end:
        return t[idx]
    mid = (start + end) // 2
    if rge_e <= mid:
        return st_product(t, rge_s, rge_e, start, mid, idx * 2)
    elif rge_s > mid:
        return st_product(t, rge_s, rge_e, mid + 1, end, idx * 2 + 1)
    else:
        return (st_product(t, rge_s, mid, start, mid, idx * 2)
                * st_product(t, mid + 1, rge_e, mid + 1, end, idx * 2 + 1)) % 1000000007


N, M, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
tree = [0 for _ in range(N * 4)]
st_init(tree, L, 0, N - 1, 1)
for _ in range(M + K):
    a, b, c = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    if a == 1:
        st_update(tree, b, c, 1, N, 1)
    elif a == 2:
        print(st_product(tree, b, c, 1, N, 1) % 1000000007)