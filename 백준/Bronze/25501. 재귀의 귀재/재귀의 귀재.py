import sys

def recursion(s, l, r, x):
    if l >= r:
        return 1, x
    elif s[l] != s[r]:
        return 0, x
    else:
        return recursion(s, l + 1, r - 1, x + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    flag, call = isPalindrome(line)
    print(flag, call)