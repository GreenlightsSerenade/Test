st = input().strip()
n = len(st)
i = 0
x = 0

while i < n:
    if st[i] == 'c':
        if i + 1 < n and (st[i + 1] == '=' or st[i + 1] == '-'):
            i += 2
        else:
            i += 1
    elif st[i] == 'd':
        if i + 1 < n and st[i + 1] == '-':
            i += 2
        elif i + 2 < n and (st[i + 1] == 'z' and st[i + 2] == '='):
            i += 3
        else:
            i += 1
    elif st[i] == 'l' or st[i] == 'n':
        if i + 1 < n and st[i + 1] == 'j':
            i += 2
        else:
            i += 1
    elif st[i] == 's' or st[i] == 'z':
        if i + 1 < n and st[i + 1] == '=':
            i += 2
        else:
            i += 1
    else:
        i += 1
    x += 1

print(x)