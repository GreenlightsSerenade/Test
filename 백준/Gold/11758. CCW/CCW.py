import sys


x1, y1 = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
x2, y2 = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
x3, y3 = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))

n = (x2 - x1) * y3 - (y2 - y1) * x3 - (x2 * y1 - y2 * x1)
if n < 0:
    print('-1')
elif n > 0:
    print('1')
else:
    print('0')