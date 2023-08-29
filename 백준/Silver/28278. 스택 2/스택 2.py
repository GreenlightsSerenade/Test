import sys

n = int(sys.stdin.readline().strip())
stck = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    if line[0] == '1':
        _, m = line.split(' ')
        stck.append(int(m))
    elif line[0] == '2':
        if stck:
            print(stck.pop())
        else:
            print('-1')
    elif line[0] == '3':
        print(len(stck))
    elif line[0] == '4':
        if stck:
            print('0')
        else:
            print('1')
    else:
        if stck:
            print(stck[-1])
        else:
            print('-1')