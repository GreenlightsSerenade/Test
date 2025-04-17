import sys
from collections import deque, defaultdict
from itertools import combinations
import heapq


N = int(sys.stdin.readline().rstrip())
L, R, M = [], [], -10001
for _ in range(N):
    A = int(sys.stdin.readline().rstrip())
    ll, lr = len(L), len(R)
    if M == -10001:
        M = A
    elif ll - lr == 0:
        if A >= M:
            heapq.heappush(R, A)
        else:
            if ll == 0:
                heapq.heappush(R, M)
                M = A
            elif (-1) * L[0] > A:
                heapq.heappush(R, M)
                M = (-1) * heapq.heappop(L)
                heapq.heappush(L, -A)
            else:
                heapq.heappush(R, M)
                M = A
    elif ll - lr == -1:
        if A >= M:
            heapq.heappush(L, -M)
            if R[0] < A:
                M = heapq.heappop(R)
                heapq.heappush(R, A)
            else:
                M = A
        else:
            heapq.heappush(L, -A)
    print(M)