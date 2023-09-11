import sys


def solution(n, nums):
    d = {}
    for elem in nums:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1

    stck = []
    ret = [(-1, -1) for _ in range(n)]

    for i in range(n):
        while stck and d[nums[i]] > d[stck[-1][0]]:
            _, pos = stck.pop()
            ret[pos] = (nums[i], pos)
        stck.append((nums[i], i))

    return ' '.join([str(e[0]) for e in ret])


print(solution(int(sys.stdin.readline().rstrip()), list(map(int, sys.stdin.readline().rstrip().split(' ')))))