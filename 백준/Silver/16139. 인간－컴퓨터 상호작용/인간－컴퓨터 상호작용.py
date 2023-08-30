import sys

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
line = sys.stdin.readline().rstrip()
length = len(line)
a_list = [[0 for _ in range(length)] for _ in range(26)]
for i in range(26):
    if alpha[i] == line[0]:
        a_list[i][0] = 1
    for j in range(1, length):
        if alpha[i] == line[j]:
            a_list[i][j] = a_list[i][j - 1] + 1
        else:
            a_list[i][j] = a_list[i][j - 1]

n = int(sys.stdin.readline().rstrip())
s = set()

for i in range(n):
    tmp = sys.stdin.readline().rstrip().split(' ')
    m = ord(tmp[0]) - ord('a')
    x, y = int(tmp[1]), int(tmp[2])
    if x == 0:
        print(a_list[m][y])
    else:
        print(a_list[m][y] - a_list[m][x - 1])