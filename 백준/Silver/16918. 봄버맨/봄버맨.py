import sys

def set_bomb(bomb_name):
    for y in range(R):
        for x in range(C):
            if board[y][x] == '.':
                board[y][x] = str(bomb_name)

def boom_bomb(bomb_time):
    for y in range(R):
        for x in range(C):
            if board[y][x] == str(bomb_time-3):
                for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                    dy, dx = y+i, x+j
                    if 0 <= dy < R and 0 <= dx < C and board[dy][dx] != board[y][x]:
                        board[dy][dx] = '.'
                board[y][x] = '.'

R, C, N = map(int, sys.stdin.readline().split())

board = []

for _ in range(R):
    temp = sys.stdin.readline().rstrip()
    temp = temp.replace('O', '0')
    board.append(list(temp))

for time in range(2, N+1):
    if time % 2 == 0:
        set_bomb(time)
    else:
        boom_bomb(time)


for y in range(R):
    for x in range(C):
        if board[y][x] != '.':
            print('O', end="")
        else:
            print(board[y][x], end="")
    print()