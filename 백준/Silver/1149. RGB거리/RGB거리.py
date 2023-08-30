import sys

def solution(rgb, n):
    DP = [[0, 0, 0] for _ in range(n + 1)]
    DP[0] = rgb[0]
    for i in range(1, n):
        DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + rgb[i][0]
        DP[i][1] = min(DP[i - 1][2], DP[i - 1][0]) + rgb[i][1]
        DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + rgb[i][2]
    return min(DP[n - 1])

n = int(sys.stdin.readline().rstrip())
rgb_list = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    rgb = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
    rgb_list[i][0], rgb_list[i][1], rgb_list[i][2] = rgb[0], rgb[1], rgb[2]

print(solution(rgb_list, n))