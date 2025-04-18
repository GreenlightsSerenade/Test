def solution(diffs, times, limit):
    length = len(diffs)
    answer = 0
    left, right = 1, max(diffs)
    while left <= right:
        mid = (left + right) // 2
        alltime, prev_time = 0, 0
        for i in range(length):
            ite = 0 if mid > diffs[i] else diffs[i] - mid
            alltime += (prev_time + times[i]) * ite + times[i]
            prev_time = times[i]
        if alltime <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer