import sys

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)
n = int(sys.stdin.readline().rstrip())
print(fib_rec(n))