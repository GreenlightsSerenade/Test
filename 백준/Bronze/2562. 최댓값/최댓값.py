import sys


mx = -1, -1
for i in range(9):
    N = int(sys.stdin.readline().rstrip())
    if N > mx[0]:
        mx = N, i + 1
print(mx[0])
print(mx[1])