from copy import deepcopy

def DFS(level, safe):
    global answer
    if level == len(cctv):
        temp = 0
        for y in range(Y):
            for x in range(X):
                if safe[y][x] != "#" and safe[y][x] < 1:
                    temp += 1
        answer = min(answer, temp)
        return

    type, ny, nx = cctv[level]

    for direction in cctv_dir[type]:
        copy_safe = deepcopy(safe)
        for idx in direction:
            temp = 1
            i, j = dir[idx]
            while True:
                dy, dx = ny+(i*temp), nx+(j*temp)
                if 0 <= dy < Y and 0 <= dx < X and (safe[dy][dx] == '#' or safe[dy][dx] < 6):
                    if safe[dy][dx] == 0:
                        safe[dy][dx] = '#'
                    temp += 1
                else:
                    break
        DFS(level+1, safe)
        safe = copy_safe

Y, X = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(Y)]

cctv = []

check = [[0]*X for _ in range(Y)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = 1e9

cctv_dir = [[],
       [
           # 1번 cctv의 회전 방향
           [0], [1], [2], [3]
       ],
       [
           # 2번 cctv의 회전 방향
           [0, 1], [2, 3]
       ],
       [
           # 3번 cctv의 회전 방향
           [0, 3], [1, 3], [1, 2], [0, 2]
       ],
       [
           # 4번 cctv의 회전 방향
           [0, 2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2]
       ],
       [
           # 5번 cctv의 회전 방향
           [0, 1, 2, 3]
       ]]

for y in range(Y):
    for x in range(X):
        if board[y][x] > 0 and board[y][x] < 6:
            cctv.append((board[y][x], y, x))

DFS(0, board)
print(answer)