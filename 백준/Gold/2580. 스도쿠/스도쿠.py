import sys

def find_not_fill():
  lst = []
  for y in range(9):
    for x in range(9):
      if not board[y][x]:
        lst.append((y, x))
  return lst

def row_fill(Y, num):
    for x in range(9):
        if board[Y][x] == num:
            return True
    return False

def col_fill(X, num):
    for y in range(9):
        if board[y][X] == num:
            return True
    return False

def ground_fill(Y, X, num):
    gy, gx = Y // 3 * 3, X // 3 * 3
    for y in range(gy, gy + 3):
        for x in range(gx, gx + 3):
            if board[y][x] == num:
                return True
    return False

def find_num(idx):
    if idx == len(not_fill):
        for i in range(9):
            print(*board[i])
        sys.exit()

    for n in range(1, 10):
        ny, nx = not_fill[idx][0], not_fill[idx][1]
        if not row_fill(ny, n) and not col_fill(nx, n) and not ground_fill(ny, nx, n):
            board[ny][nx] = n
            find_num(idx + 1)
            board[ny][nx] = 0


inputs = sys.stdin.readline

board = [list(map(int, inputs().split())) for _ in range(9)]

not_fill = find_not_fill()

find_num(0)
