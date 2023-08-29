import sys

n = int(sys.stdin.readline().rstrip())

lst1 = sys.stdin.readline().rstrip().split(' ')
lst2 = sys.stdin.readline().rstrip().split(' ')

q = []
for i in range(n):
    if lst1[n - i - 1] == '0':
        q.append(lst2[n - i - 1])

m = int(sys.stdin.readline().rstrip())
lst = sys.stdin.readline().rstrip().split(' ')
for elem in lst:
    q.append(elem)

sys.stdout.write(' '.join(q[:m]))