import sys


nums = [0 for _ in range(10001)]
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    nums[int(sys.stdin.readline().rstrip())] += 1
for i in range(1, 10001):
    if nums[i] > 0:
        for _ in range(nums[i]):
            print(i)