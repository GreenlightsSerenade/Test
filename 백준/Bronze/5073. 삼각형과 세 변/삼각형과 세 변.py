import sys


def solution(x):
    a, b, c = x[0], x[1], x[2]
    if c >= a + b:
        return 'Invalid'
    elif a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or c == a:
        return 'Isosceles'
    else:
        return 'Scalene'


while True:
    line = sys.stdin.readline().rstrip()
    if line == '0 0 0':
        break
    print(solution(sorted(list(map(int, line.split(' '))))))