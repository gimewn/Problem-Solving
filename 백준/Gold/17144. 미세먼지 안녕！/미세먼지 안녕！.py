import sys

input = sys.stdin.readline

def spread_dust():
    temp = [[0]*Y for _ in range(X)]
    for x in range(X):
        for y in range(Y):
            if board[x][y] >= 5:
                cnt = 0
                for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                    dx, dy = x + i, y + j
                    if 0 <= dx < X and 0 <= dy < Y and board[dx][dy] >= 0:
                        temp[dx][dy] += board[x][y] // 5
                        cnt += 1
                temp[x][y] -= board[x][y]//5*cnt
    for x in range(X):
        for y in range(Y):
            board[x][y] += temp[x][y]

def on_clean(dir):
    cx, cy = air_clean[dir]
    if dir == 0:
        # ⬇️
        for x in range(cx-2, -1, -1):
            board[x+1][0] = board[x][0]
        # ⬅️
        for y in range(1, Y):
            board[0][y-1] = board[0][y]
        # ⬆️
        for x in range(1, cx+1):
            board[x-1][Y-1] = board[x][Y-1]
        # ➡️
        for y in range(Y-2, 0, -1):
            board[cx][y+1] = board[cx][y]
        # 공청기에 빨려들어간 먼지는 정화됨
    else:
        # ⬆️
        for x in range(cx + 2, X):
            board[x - 1][0] = board[x][0]
        # ⬅️
        for y in range(1, Y):
            board[X - 1][y - 1] = board[X - 1][y]
        # ⬇️
        for x in range(X - 2, cx - 1, -1):
            board[x + 1][Y - 1] = board[x][Y - 1]
        # ➡️
        for y in range(Y - 2, 0, -1):
            board[cx][y + 1] = board[cx][y]
    board[cx][1] = 0

X, Y, T = map(int, input().split())

air_clean = []

board = []

for x in range(X):
    lst = list(map(int, input().split()))
    if not air_clean:
        if lst[0] == -1:
            air_clean = [(x, 0), (x+1, 0)]
    board.append(lst)

for now in range(T):
    # 1. 먼지가 확산된다.
    spread_dust()
    # 공기청정기가 작동한다.
    # 위쪽은 반시계방향
    on_clean(0)
    # 아래쪽은 시계방향
    on_clean(1)

answer = 0

for x in range(X):
    for y in range(Y):
        if board[x][y] > 0:
            answer += board[x][y]

print(answer)