def solution(x, y, n):
    MAX = 9999999
    DP = [MAX for _ in range(y + 1)]
    DP[x] = 0
    for i in range(x + 1, y + 1):
        a, b = MAX, MAX
        if i % 2 == 0:
            a = DP[i // 2]
        if i % 3 == 0:
            b = DP[i // 3]
        DP[i] = min(DP[i - n], a, b) + 1
    return DP[y] if DP[y] < MAX else -1