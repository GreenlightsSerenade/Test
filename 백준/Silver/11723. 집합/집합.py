import sys


def solution(n):
    S = 0
    for _ in range(n):
        lines = sys.stdin.readline().rstrip().split(' ')
        if lines[0][0] == 'r': # remove
            x = int(lines[1])
            S &= ~(1 << (x - 1))
        elif lines[0][0] == 'c': # check
            x = int(lines[1])
            print((S & (1 << (x - 1))) >> (x - 1))
        elif lines[0][0] == 't': # toggle
            x = int(lines[1])
            S ^= (1 << (x - 1))
        elif lines[0][0] == 'e': # empty
            S = 0
        elif lines[0][0] == 'a' and lines[0][1] == 'd': # add
            x = int(lines[1])
            S |= (1 << (x - 1))
        else: # all
            S = 2 ** 20 - 1


N = int(sys.stdin.readline().rstrip())
solution(N)