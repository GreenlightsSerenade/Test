n = int(input())
ret = 0

for i in range(n):
    line = input()
    d = dict()
    flag = True
    for j in range(len(line)):
        if line[j] not in d or line[j] == line[j - 1]:
            d[line[j]] = 0
        else:
            flag = False
            break
    if flag:
        ret += 1

print(ret)