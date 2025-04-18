from collections import deque

def solution(plans):
    plans.sort(key=lambda x: x[1])
    n = len(plans)
    tmp = plans[0][1].split(':')
    st = int(tmp[0]) * 60 + int(tmp[1])
    lst = deque([])
    for plan in plans:
        tmp = plan[1].split(':')
        time = int(tmp[0]) * 60 + int(tmp[1]) - st
        lst.append((plan[0], time, int(plan[2])))
    name, _, playtime = lst.popleft()
    remain = []
    time = 0
    answer = []
    while len(answer) < n:
        fintime = time + playtime
        if len(lst) == 0:
            answer.append(name)
            break
        elif fintime == lst[0][1] or (fintime < lst[0][1] and len(remain) == 0):
            answer.append(name)
            name, time, playtime = lst.popleft()
        elif fintime < lst[0][1] and len(remain) != 0:
            answer.append(name)
            name, _, playtime = remain.pop()
            time = fintime
        else:
            remain.append((name, None, playtime - (lst[0][1] - time)))
            name, time, playtime = lst.popleft()
    while lst:
        name, _, _ = lst.popleft()
        answer.append(name)
    while remain:
        name, _, _ = remain.pop()
        answer.append(name)

    return answer