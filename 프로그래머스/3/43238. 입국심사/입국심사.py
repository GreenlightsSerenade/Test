def solution(n, times):
    mn, mx = min(times), max(times) * n
    answer = 0
    while mn <= mx:
        mid = (mn + mx) // 2
        u = 0
        for t in times:
            u += (mid // t)
            if u >= n:
                break
        if u >= n:
            answer = mid
            mx = mid - 1
        else:
            mn = mid + 1
    return answer