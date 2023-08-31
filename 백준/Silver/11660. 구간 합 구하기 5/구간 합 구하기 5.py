import sys

n, m = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
sum_table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
lst = [0 for _ in range(n)]
for i in range(1, n + 1):
    lst = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    tmp = 0
    for j in range(1, n + 1):
        sum_table[i][j] = tmp + lst[j - 1] + sum_table[i - 1][j]
        tmp += lst[j - 1]

for _ in range(m):
    x1, y1, x2, y2 = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    print(sum_table[x2][y2] - sum_table[x2][y1 - 1] - sum_table[x1 - 1][y2] + sum_table[x1 - 1][y1 - 1])
