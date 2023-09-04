import sys
from collections import deque


def solution(n, k):
    if n == k:
        return 0
    cnt = 0
    dq = deque([n])
    check = [True for _ in range(100001)]
    check[n] = False
    flag = False
    while dq:
        length = len(dq)
        for _ in range(length):
            now = dq.popleft()
            if 0 <= now - 1 <= 100000 and check[now - 1]:
                if now - 1 == k:
                    flag = True
                    break
                else:
                    dq.append(now - 1)
                    check[now - 1] = False
            if 0 <= now + 1 <= 100000 and check[now + 1]:
                if now + 1 == k:
                    flag = True
                    break
                else:
                    dq.append(now + 1)
                    check[now + 1] = False
            if 0 <= 2 * now <= 100000 and check[2 * now]:
                if 2 * now == k:
                    flag = True
                    break
                else:
                    dq.append(2 * now)
                    check[2 * now] = False
        cnt += 1
        if flag:
            break
    return cnt


N, K = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))
print(solution(N, K))