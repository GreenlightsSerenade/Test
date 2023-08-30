import sys

def wanderer(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    w = [[[1 for _ in range(22)] for _ in range(22)] for _ in range(22)]
    if a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                if i < j and j < k:
                    w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
                else:
                    w[i][j][k] = w[i - 1][j][k] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]
    return w[a][b][c]

while True:
    line = sys.stdin.readline().rstrip()
    if line == '-1 -1 -1':
        break
    line = tuple(map(int, line.split(' ')))
    print('w({}, {}, {}) = {}'.format(line[0], line[1], line[2], wanderer(line[0], line[1], line[2])))
