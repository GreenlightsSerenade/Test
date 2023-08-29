import sys

line = sys.stdin.readline().strip()

x, n = line.split(' ')
n = int(n)
l = len(x)

sum = 0
tmp = 1
for i in range(l):
    temp = ord(x[l - i - 1])
    if temp < 60:
        sum += tmp * (temp - 48)
    else:
        sum += tmp * (temp - 55)
    tmp *= n
print(sum)