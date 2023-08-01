import sys
sys.setrecursionlimit(10**9)

def findSafeGround(h):
    def dfs(sx, sy):
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = sx + i, sy + j
            if 0 > dx or dx >= N or 0 > dy or dy >= N:
                continue
            if check[dx][dy]:
                continue
            if board[dx][dy] > h:
                check[dx][dy] = 1
                dfs(dx, dy)

    check = [[0]*N for _ in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if check[x][y]:
                continue
            if board[x][y] <= h:
                continue
            check[x][y] = 1
            count += 1
            dfs(x, y)

    return count

N = int(input())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
maxHeight = max(max(board))

# 잠기지 않을 경우 => 안전구역 1개
answer = 1

for height in range(1, 101):
    answer = max(answer, findSafeGround(height))

print(answer)