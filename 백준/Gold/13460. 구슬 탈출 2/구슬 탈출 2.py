import sys
from collections import deque


def solution(N, M, maps):
    red = [0, 0]
    blue = [0, 0]
    hole = [0, 0]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if maps[i][j] == 'R':
                red[0], red[1] = i, j
            elif maps[i][j] == 'B':
                blue[0], blue[1] = i, j
            elif maps[i][j] == 'O':
                hole[0], hole[1] = i, j

    def grav(pos, dir):
        red_y, red_x, blue_y, blue_x = pos
        win_flag = False
        if dir == 0: # leftgrav
            if blue_x < red_x and blue_y == red_y:
                while blue_x > 1:
                    if maps[blue_y][blue_x - 1] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y][blue_x - 1] == '#':
                        break
                    else:
                        blue_x -= 1
                while red_x > 1:
                    if maps[red_y][red_x - 1] == 'O':
                        return [(-1, -1, -1, -1)], 1
                    elif maps[red_y][red_x - 1] == '#' or red_x - 1 == blue_x:
                        break
                    else:
                        red_x -= 1
            else:
                while red_x > 1:
                    if maps[red_y][red_x - 1] == 'O':
                        win_flag = True
                        red_x, red_y = -1, -1
                        break
                    elif maps[red_y][red_x - 1] == '#':
                        break
                    else:
                        red_x -= 1
                while blue_x > 1:
                    if maps[blue_y][blue_x - 1] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y][blue_x - 1] == '#' or (blue_x - 1 == red_x and blue_y == red_y):
                        break
                    else:
                        blue_x -= 1
                if win_flag:
                    return [(-1, -1, -1, -1)], 1

        elif dir == 1: # rightgrav
            if blue_x > red_x and blue_y == red_y:
                while blue_x < M - 2:
                    if maps[blue_y][blue_x + 1] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y][blue_x + 1] == '#':
                        break
                    else:
                        blue_x += 1
                while red_x < M - 2:
                    if maps[red_y][red_x + 1] == 'O':
                        return [(-1, -1, -1, -1)], 1
                    elif maps[red_y][red_x + 1] == '#' or red_x + 1 == blue_x:
                        break
                    else:
                        red_x += 1
            else:
                while red_x < M - 2:
                    if maps[red_y][red_x + 1] == 'O':
                        win_flag = True
                        red_x, red_y = -1, -1
                        break
                    elif maps[red_y][red_x + 1] == '#':
                        break
                    else:
                        red_x += 1
                while blue_x < M - 2:
                    if maps[blue_y][blue_x + 1] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y][blue_x + 1] == '#' or (blue_x + 1 == red_x and blue_y == red_y):
                        break
                    else:
                        blue_x += 1
                if win_flag:
                    return [(-1, -1, -1, -1)], 1
        elif dir == 2: # upgrav
            if blue_x == red_x and blue_y < red_y:
                while blue_y > 1:
                    if maps[blue_y - 1][blue_x] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y - 1][blue_x] == '#':
                        break
                    else:
                        blue_y -= 1
                while red_y > 1:
                    if maps[red_y - 1][red_x] == 'O':
                        return [(-1, -1, -1, -1)], 1
                    elif maps[red_y - 1][red_x] == '#' or red_y - 1 == blue_y:
                        break
                    else:
                        red_y -= 1
            else:
                while red_y > 1:
                    if maps[red_y - 1][red_x] == 'O':
                        win_flag = True
                        red_x, red_y = -1, -1
                        break
                    elif maps[red_y - 1][red_x] == '#':
                        break
                    else:
                        red_y -= 1
                while blue_y > 1:
                    if maps[blue_y - 1][blue_x] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y - 1][blue_x] == '#' or (blue_y - 1 == red_y and blue_x == red_x):
                        break
                    else:
                        blue_y -= 1
                if win_flag:
                    return [(-1, -1, -1, -1)], 1
        elif dir == 3: # downgrav
            if blue_x == red_x and blue_y > red_y:
                while blue_y < N - 2:
                    if maps[blue_y + 1][blue_x] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y + 1][blue_x] == '#':
                        break
                    else:
                        blue_y += 1
                while red_y < N - 2:
                    if maps[red_y + 1][red_x] == 'O':
                        return [(-1, -1, -1, -1)], 1
                    elif maps[red_y + 1][red_x] == '#' or red_y + 1 == blue_y:
                        break
                    else:
                        red_y += 1
            else:
                while red_y < N - 2:
                    if maps[red_y + 1][red_x] == 'O':
                        win_flag = True
                        red_x, red_y = -1, -1
                        break
                    elif maps[red_y + 1][red_x] == '#':
                        break
                    else:
                        red_y += 1
                while blue_y < N - 2:
                    if maps[blue_y + 1][blue_x] == 'O':
                        return [(-1, -1, -1, -1)], -1
                    elif maps[blue_y + 1][blue_x] == '#' or (blue_y + 1 == red_y and blue_x == red_x):
                        break
                    else:
                        blue_y += 1
                if win_flag:
                    return [(-1, -1, -1, -1)], 1
        return (red_y, red_x, blue_y, blue_x), 0

    stck = deque([(red[0], red[1], blue[0], blue[1])])
    flag = {}
    ans = 0
    while stck:
        ans += 1
        if ans == 11:
            return -1
        l = len(stck)
        for _ in range(l):
            elem = stck.popleft()
            flag[elem] = True
            for i in range(4):
                value, check = grav(elem, i)
                if check == -1:
                    continue
                elif check == 1:
                    return ans
                elif value in flag:
                    continue
                else:
                    stck.append(value)
                    flag[value] = True
        #print(ans, stck, flag.keys())
    return -1


N, M = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
maping = deque()
for _ in range(N):
    maping.append(list(sys.stdin.readline().rstrip()))
print(solution(N, M, maping))
# tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
# list(map(int, sys.stdin.readline().rstrip().split(' ')))
# N = int(sys.stdin.readline().rstrip())
# line = sys.stdin.readline().rstrip()
