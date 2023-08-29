from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
deq = deque()

for _ in range(n):
    line = sys.stdin.readline().rstrip().split(' ')
    if line[0] == '1':
        deq.appendleft(int(line[1]))
    elif line[0] == '2':
        deq.append(int(line[1]))
    elif line[0] == '3':
        if deq:
            print(deq.popleft())
        else:
            print('-1')
    elif line[0] == '4':
        if deq:
            print(deq.pop())
        else:
            print('-1')
    elif line[0] == '5':
        print(len(deq))
    elif line[0] == '6':
        if deq:
            print('0')
        else:
            print('1')
    elif line[0] == '7':
        if deq:
            print(deq[0])
        else:
            print('-1')
    elif line[0] == '8':
        if deq:
            print(deq[-1])
        else:
            print('-1')
