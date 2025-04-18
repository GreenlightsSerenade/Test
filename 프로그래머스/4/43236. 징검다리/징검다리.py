def solution(distance, rocks, n):
    rocks.sort()
    num = len(rocks)
    left, right = 0, distance
    dis = [rocks[0]]
    for i in range(1, num):
        dis.append(rocks[i] - rocks[i - 1])
    dis.append(distance - rocks[-1])
    while left <= right:
        mid = (left + right) // 2
        tmp, cnt = 0, 0
        for d in dis:
            tmp += d
            if mid <= tmp:
                tmp = 0
            else:
                cnt += 1
        if cnt <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    return answer