import sys


def solution(n):
    nums = [[0, -1] for _ in range(n + 1)]
    for i in range(n - 1, 0, -1):
        a, b, c = n + 1, n + 1, n + 1
        if i * 3 <= n:
            a = nums[i * 3][0]
        if i * 2 <= n:
            b = nums[i * 2][0]
        c = nums[i + 1][0]
        nums[i][0] = min(a, b, c) + 1
        if nums[i][0] == a + 1 and i * 3 <= n:
            nums[i][1] = i * 3
        elif nums[i][0] == b + 1 and i * 2 <= n:
            nums[i][1] = i * 2
        else:
            nums[i][1] = i + 1
    print(nums[1][0])
    x = [1]
    while nums[x[-1]][1] != -1:
        x.append(nums[x[-1]][1])
    print(' '.join(map(str, x[::-1])))


N = int(sys.stdin.readline().rstrip())
solution(N)