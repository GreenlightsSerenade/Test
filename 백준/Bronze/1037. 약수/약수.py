import sys

n = int(sys.stdin.readline().rstrip())
lst = sorted(list(map(int, sys.stdin.readline().rstrip().split(' '))))

if n % 2 == 0:
    print(lst[n // 2 - 1] * lst[n // 2])
else:
    print(lst[n // 2] ** 2)