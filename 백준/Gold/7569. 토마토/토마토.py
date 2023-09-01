import sys
from collections import deque


def solution(length, width, height, box):
    q = deque()
    no = 0
    answer = 0
    for i in range(height):
        for j in range(width):
            for k in range(length):
                if box[i][j][k] == 0:
                    no += 1
                elif box[i][j][k] == 1:
                    q.append((i, j, k))
    if no == 0:
        return answer
    while q and no > 0:
        ql = len(q)
        for _ in range(ql):
            x, y, z = q.popleft()
            if x > 0 and box[x - 1][y][z] == 0:
                no -= 1
                box[x - 1][y][z] = 1
                q.append((x - 1, y, z))
            if x < height - 1 and box[x + 1][y][z] == 0:
                no -= 1
                box[x + 1][y][z] = 1
                q.append((x + 1, y, z))
            if y > 0 and box[x][y - 1][z] == 0:
                no -= 1
                box[x][y - 1][z] = 1
                q.append((x, y - 1, z))
            if y < width - 1 and box[x][y + 1][z] == 0:
                no -= 1
                box[x][y + 1][z] = 1
                q.append((x, y + 1, z))
            if z > 0 and box[x][y][z - 1] == 0:
                no -= 1
                box[x][y][z - 1] = 1
                q.append((x, y, z - 1))
            if z < length - 1 and box[x][y][z + 1] == 0:
                no -= 1
                box[x][y][z + 1] = 1
                q.append((x, y, z + 1))
        answer += 1
    if no > 0:
        return -1
    return answer


M, N, H = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
B = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        B[i][j] = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(solution(M, N, H, B))