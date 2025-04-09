import sys


def solution(N, M, x, y, K, maps, says):
    dxdy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    dice_move = [(2, 1, 5, 0, 4, 3),
                 (3, 1, 0, 5, 4, 2),
                 (4, 0, 2, 3, 5, 1),
                 (1, 5, 2, 3, 0, 4)]
    dice = [0, 0, 0, 0, 0, 0]
    pos = [x, y]
    for s in says:
        elem = s - 1
        if not ((0 <= pos[0] + dxdy[elem][0] < N) and (0 <= pos[1] + dxdy[elem][1] < M)):
            continue
        pos[0] = pos[0] + dxdy[elem][0]
        pos[1] = pos[1] + dxdy[elem][1]
        tmp = dice_move[elem]
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = (
            dice[tmp[0]], dice[tmp[1]], dice[tmp[2]], dice[tmp[3]], dice[tmp[4]], dice[tmp[5]])
        if maps[pos[0]][pos[1]] == 0:
            maps[pos[0]][pos[1]] = dice[5]
        else:
            dice[5] = maps[pos[0]][pos[1]]
            maps[pos[0]][pos[1]] = 0
        print(dice[0])


N, M, x, y, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
maping = []
for _ in range(N):
    maping.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))
say = list(map(int, sys.stdin.readline().rstrip().split(' ')))
solution(N, M, x, y, K, maping, say)