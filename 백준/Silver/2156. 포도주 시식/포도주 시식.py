import sys

def solution(n, wine):
    if n == 1:
        return wine[0]
    elif n == 2:
        return wine[0] + wine[1]
    DP = [0 for _ in range(n)]
    DP[0] = wine[0]
    DP[1] = wine[0] + wine[1]

    flag = False
    DP[2] = max(wine[0] + wine[1], wine[1] + wine[2], wine[2] + wine[0])
    if DP[2] == wine[1] + wine[2]:
        flag = True
    for i in range(3, n):
        if flag:
            tmp = max(DP[i - 3] + wine[i - 1] + wine[i],
                      DP[i - 2] + wine[i],
                      DP[i - 1])
            if tmp != DP[i - 3] + wine[i - 1] + wine[i]:
                flag = False
            DP[i] = tmp
        else:
            if DP[i - 1] > DP[i - 2]:
                DP[i] = DP[i - 1] + wine[i]
                flag = True
            else:
                DP[i] = DP[i - 2] + wine[i]
    return DP[-1]


n = int(sys.stdin.readline().rstrip())
wine = [0 for _ in range(n)]
for i in range(n):
    wine[i] = int(sys.stdin.readline().rstrip())

print(solution(n, wine))