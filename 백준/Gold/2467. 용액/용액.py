import sys


def solution(n, nums):
    left, right = 0, n - 1
    chk = 10 ** 15
    ret_l, ret_r = 0, n - 1
    while left < right:
        if nums[left] + nums[right] == 0:
            return str(nums[left]) + ' ' + str(nums[right])
        if abs(chk) > abs(nums[left] + nums[right]):
            ret_l, ret_r = left, right
            chk = nums[left] + nums[right]
        if nums[left] + nums[right] > 0:
            right -= 1
        else:
            left += 1
    return str(nums[ret_l]) + ' ' + str(nums[ret_r])


N = int(sys.stdin.readline().rstrip())
print(solution(N, sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))))))