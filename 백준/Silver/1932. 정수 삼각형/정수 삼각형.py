import sys

N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
check = [[0]*(idx+1) for idx in range(N)]
check[-1] = board[-1]

for y in range(N-1, 0, -1):
    for x in range(y+1):
        if x-1 >= 0:
            check[y-1][x-1] = max(check[y-1][x-1], check[y][x] + board[y-1][x-1])
        if x < y:
            check[y-1][x] = max(check[y-1][x], check[y][x] + board[y-1][x])

print(check[0][0])