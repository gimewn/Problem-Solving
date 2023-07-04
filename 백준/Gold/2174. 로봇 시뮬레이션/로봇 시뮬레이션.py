import sys

inputs = sys.stdin.readline

dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

rot = [[2, 1], [0, 3], [3, 0], [1, 2]]

def do_prompt(idx, now_prompot, now_count):
    if now_prompot == 'L' or now_prompot == 'R':
        column = 0
        if now_prompot == 'R':
            column = 1
        now_count %= 4
        now_dir = robots[idx][2]
        for _ in range(now_count):
            now_dir = rot[now_dir][column]
        robots[idx] = (robots[idx][0], robots[idx][1], now_dir)

    elif now_prompot == 'F':
        ny, nx, ndir = robots[idx][0], robots[idx][1], robots[idx][2]
        ty, tx = ny, nx
        for _ in range(now_count):
            dy, dx = ty + dir[ndir][0], tx + dir[ndir][1]
            if 0 >= dy or dy > B or 0 >= dx or dx > A:
                print(f'Robot {idx} crashes into the wall')
                exit(0)
            elif board[dy][dx]:
                print(f'Robot {idx} crashes into robot {board[dy][dx]}')
                exit(0)
            ty, tx = dy, dx

        board[ny][nx] = 0
        board[dy][dx] = idx
        robots[idx] = (dy, dx, ndir)

A, B = map(int, inputs().split())

N, M = map(int, inputs().split())

board = [[0]*(A+1) for _ in range(B+1)]

robots = [0]

for idx in range(N):
    x, y, d = inputs().split()
    x = int(x)
    y = int(y)
    if d == 'N':
        d_to_int = 0
    elif d == 'E':
        d_to_int = 1
    elif d == 'W':
        d_to_int = 2
    elif d == 'S':
        d_to_int = 3
    robots.append((y, x, d_to_int))
    board[y][x] = idx+1

for _ in range(M):
    num, prompt, count = inputs().split()
    do_prompt(int(num), prompt, int(count))

print("OK")