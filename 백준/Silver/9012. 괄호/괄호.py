import sys

n = int(sys.stdin.readline().strip())
for _ in range(n):
    line = sys.stdin.readline().strip()
    stck = []
    flag = False
    for letter in line:
        if letter == '(':
            stck.append('(')
        else:
            if stck:
                stck.pop()
            else:
                flag = True
                break
    if flag or stck:
        print('NO')
    else:
        print('YES')