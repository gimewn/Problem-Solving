import sys
from collections import deque

inputs = sys.stdin.readline
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def rain_magic():

    def sum_amount():
        amount = 0
        for y in range(N):
            for x in range(N):
                amount += board[y][x]
        return amount

    def find_new_cloud():
        new_cloud = set()
        for y in range(N):
            for x in range(N):
                if board[y][x] >= 2:
                    if (y, x) not in cloud:
                        new_cloud.add((y, x))
                        board[y][x] -= 2
        return new_cloud

    def check_water():
        for cy, cx in cloud:
            cnt = 0
            for idx in (2, 4, 6, 8):
                i, j = dir[idx]
                dy, dx = cy+i, cx+j
                if 0 <= dy < N and 0 <= dx < N and board[dy][dx]:
                   cnt += 1
            board[cy][cx] += cnt

    def move_cloud(d, s):
        new_cloud = set()
        while cloud:
            cy, cx = cloud.pop()
            ncy, ncx = (cy + dir[d][0] * s) % N, (cx + dir[d][1] * s) % N
            board[ncy][ncx] += 1
            new_cloud.add((ncy, ncx))
        return new_cloud

    N, M = map(int, inputs().split())
    board = [list(map(int, inputs().split())) for _ in range(N)]

    # 초기 구름 위치
    cloud = set([(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)])

    for _ in range(M):
        D, S = map(int, inputs().split())
        cloud = move_cloud(D, S)
        check_water()
        cloud = find_new_cloud()

    print(sum_amount())

rain_magic()