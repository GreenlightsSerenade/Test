import sys

def solution(n):
    for i in range(n):
        for j in range(n):
            flag = True
            a, b = n, n // 3
            while flag and b > 0:
                if (i % a) // b == 1 and (j % a) // b == 1:
                    flag = False
                    break
                a, b = b, b // 3
            if not flag:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('*')
        sys.stdout.write('\n')

N = int(sys.stdin.readline().rstrip())
solution(N)