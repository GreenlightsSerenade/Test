import sys

def backtrack(pos, cnt, stp, row, col, squ):
    if cnt == stp:
        return True
    y, x = pos[cnt][0], pos[cnt][1]
    z = (y // 3) * 3 + x // 3
    tmp = row[y] & col[x] & squ[z]
    if not tmp:
        return False
    for elem in tmp:
        row[y].remove(elem)
        col[x].remove(elem)
        squ[z].remove(elem)
        pos[cnt][2] = elem
        if backtrack(pos, cnt + 1, stp, row, col, squ):
            return True
        row[y].add(elem)
        col[x].add(elem)
        squ[z].add(elem)

def solution_sudoku(board):
    row_c = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    col_c = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    squ_c = [{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)]
    pos = []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                tmp = {board[i][j]}
                row_c[i] -= tmp
                col_c[j] -= tmp
                squ_c[(i // 3) * 3 + j // 3] -= tmp
            else:
                pos.append([i, j, 0])
    n = len(pos)
    if backtrack(pos, 0, n, row_c, col_c, squ_c):
        for elem in pos:
            board[elem[0]][elem[1]] = elem[2]
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = "")
            if j == 8:
                print()
            else:
                print("", end = " ")


board = [[0 for _ in range(9)] for _ in range(9)]
for i in range(9):
    board[i] = list(map(int, sys.stdin.readline().rstrip().split(' ')))
solution_sudoku(board)