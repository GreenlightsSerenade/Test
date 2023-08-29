import sys

n = int(sys.stdin.readline().rstrip())
q = [0 for _ in range(2000001)]
front, rear = 0, 0

for _ in range(n):
    line = sys.stdin.readline().rstrip().split(' ')
    if line[0] == 'push':
        q[rear] = int(line[1])
        rear += 1
    elif line[0] == 'pop':
        if front != rear:
            print(q[front])
            front += 1
        else:
            print('-1')
    elif line[0] == 'size':
        print(rear - front)
    elif line[0] == 'empty':
        if front != rear:
            print('0')
        else:
            print('1')
    elif line[0] == 'front':
        if front != rear:
            print(q[front])
        else:
            print('-1')
    elif line[0] == 'back':
        if front != rear:
            print(q[rear - 1])
        else:
            print('-1')
    else:
        pass