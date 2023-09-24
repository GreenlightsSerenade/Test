import sys


def solution(n, nums):
    ans = [0 for _ in range(n + 1)]
    cnt = 0
    for num in nums:
        if num > ans[cnt]:
            cnt += 1
            ans[cnt] = num
        elif num < ans[cnt]:
            flag = True
            left, right, mid = 1, cnt, 0
            while left <= right:
                mid = (left + right) // 2
                if num == ans[mid]:
                    flag = False
                    break
                elif num > ans[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if flag:
                if ans[mid] < num:
                    ans[mid + 1] = num
                else:
                    ans[mid] = num
    return cnt


N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, L))