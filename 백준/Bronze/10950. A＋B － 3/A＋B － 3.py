def solution(n):
    for i in range(n):
        x = input().strip().split(' ')
        print(int(x[0]) + int(x[1]))


n = int(input())
solution(n)