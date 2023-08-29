import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    money = int(sys.stdin.readline().strip())
    sys.stdout.write(str(money // 25) + ' ')
    money %= 25
    sys.stdout.write(str(money // 10) + ' ')
    money %= 10
    sys.stdout.write(str(money // 5) + ' ')
    money %= 5
    sys.stdout.write(str(money // 1) + '\n')