import sys


def productwo(num, m1, m2=None):
    if m2 is None:
        m2 = m1
    tmp = [[0 for _ in range(num)] for _ in range(num)]
    for x in range(num):
        for i in range(num):
            for j in range(num):
                tmp[i][j] = (tmp[i][j] + m1[i][x] * m2[x][j]) % 1000000007
    return tmp


def recur(num, b, matrix):
    if b == 1:
        return matrix
    if b == 2:
        return productwo(num, matrix)
    if b % 2 == 0:
        return productwo(num, recur(num, b // 2, matrix))
    else:
        return productwo(num, productwo(num, recur(num, b // 2, matrix)), matrix)


def solution(num, b, matrix):
    return recur(num, b, matrix)


N = int(sys.stdin.readline().rstrip())
FIB = [[1, 1], [1, 0]]
print(recur(2, N, FIB)[0][1])