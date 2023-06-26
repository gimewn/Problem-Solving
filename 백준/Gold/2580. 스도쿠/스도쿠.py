import sys

# 숫자 비워져 있는 칸 찾기
def find_not_fill():
  lst = []
  for y in range(9):
    for x in range(9):
      if not board[y][x]:
        lst.append((y, x))
  return lst

# 해당 행에 들어 있는 숫자인지 확인
def row_fill(Y, num):
    for x in range(9):
        if board[Y][x] == num:
            return True
    return False

# 해당 열에 들어 있는 숫자인지 확인
def col_fill(X, num):
    for y in range(9):
        if board[y][X] == num:
            return True
    return False

# 해당 구역(3*3)에 들어 있는 숫자인지 확인
def ground_fill(Y, X, num):
    gy, gx = Y // 3 * 3, X // 3 * 3
    for y in range(gy, gy + 3):
        for x in range(gx, gx + 3):
            if board[y][x] == num:
                return True
    return False

def find_num(idx):
    # 인덱스가 not_fill의 길이와 같다 => 모든 빈 곳 다 채웠다
    # 프린트하고 종료시키기
    if idx == len(not_fill):
        for i in range(9):
            print(*board[i])
        sys.exit()
      
    for n in range(1, 10):
        ny, nx = not_fill[idx][0], not_fill[idx][1]
        if row_fill(ny, n):
            continue
        if col_fill(nx, n):
            continue
        if ground_fill(ny, nx, n):
            continue
            
        board[ny][nx] = n
        find_num(idx+1)
        board[ny][nx] = 0


inputs = sys.stdin.readline

board = [list(map(int, inputs().split())) for _ in range(9)]

not_fill = find_not_fill()

find_num(0)
