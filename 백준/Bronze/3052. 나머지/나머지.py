import sys

print(len(set([int(sys.stdin.readline().rstrip()) % 42 for _ in range(10)])))