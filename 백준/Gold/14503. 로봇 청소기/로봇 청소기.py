import sys


def solution(n, m, start, d, flo):
    pos_x, pos_y = start
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = 0
    while True:
        if flo[pos_x][pos_y] == 0:
            flo[pos_x][pos_y] = 2
            ans += 1
        flag = False
        for dx, dy in dxy:
            if 0 <= pos_x + dx < n and 0 <= pos_y + dy < m and flo[pos_x + dx][pos_y + dy] == 0:
                flag = True
        if flag:
            d = (d - 1) % 4
            while not (0 <= pos_x + dxy[d][0] < n and 0 <= pos_y + dxy[d][1] < m
                       and flo[pos_x + dxy[d][0]][pos_y + dxy[d][1]] == 0):
                d = (d - 1) % 4
            pos_x += dxy[d][0]
            pos_y += dxy[d][1]
        else:
            dd = (d + 2) % 4
            if (0 <= pos_x + dxy[dd][0] < n and 0 <= pos_y + dxy[dd][1] < m
                    and flo[pos_x + dxy[dd][0]][pos_y + dxy[dd][1]] == 1):
                return ans
            else:
                pos_x += dxy[dd][0]
                pos_y += dxy[dd][1]


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
R, C, D = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
L = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(N)]
print(solution(N, M, (R, C), D, L))