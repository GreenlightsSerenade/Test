import sys

line = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
d = dict()
lst = []
tple = None

for _ in range(n):
    tmp = sys.stdin.readline().rstrip().split(' ')
    tple = tmp[0], int(tmp[1]), int(tmp[2])
    if tple[0] in d:
        d[tple[0]].append((tple[1], tple[2]))
    else:
        d[tple[0]] = [(tple[1], tple[2])]
    lst.append(tple)

l = len(line)
d2 = dict()
for key in d.keys():
    d2[key] = [0 for _ in range(l)]
    if key == line[0]:
        d2[key][0] = 1
    for i in range(1, l):
        if key == line[i]:
            d2[key][i] = d2[key][i - 1] + 1
        else:
            d2[key][i] = d2[key][i - 1]

for elem in lst:
    if elem[1] == 0:
        print(d2[elem[0]][elem[2]])
    else:
        print(d2[elem[0]][elem[2]] - d2[elem[0]][elem[1] - 1])