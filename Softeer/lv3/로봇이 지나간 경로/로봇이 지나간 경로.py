import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
dir_char = ['^', '<', 'v', '>']
dot = []
visited = [[False] * W for _ in range(H)]


def check(i, j):
    cnt = 0
    result = 0
    for idx in range(4):
        di, dj = i + dir[idx][0], j + dir[idx][1]
        if 0 <= di < H and 0 <= dj < W and board[di][dj] == '#':
            cnt += 1
            result = idx
    if cnt > 1:
        return False
    return result


def BFS(y, x, direction):
    q = deque()
    path = [direction]
    q.append((y, x))
    visited[y][x] = True

    while q:
        ny, nx = q.popleft()
        for idx in range(4):
            dy, dx = ny + dir[idx][0], nx + dir[idx][1]
            if 0 <= dy < H and 0 <= dx < W and board[dy][dx] == '#' and visited[dy][dx] is False:
                path.append(idx)
                visited[dy][dx] = True
                q.append((dy, dx))
    return path


for row in range(H):
    for col in range(W):
        if board[row][col] == '#':
            res = check(row, col)
            if res is not False:
                print(row+1, col+1)
                print(dir_char[res])
                ans_path = BFS(row, col, res)
                cur = ans_path.pop(0)
                count = 1
                ans = ''

                for next in ans_path:
                    if cur == next:
                        count += 1
                        if count == 2:
                            ans += 'A'
                            count = 0
                    else:
                        if (cur + 1) % 4 == next:
                            ans += 'L'
                        else:
                            ans += 'R'
                        count = 1
                    cur = next

                print(ans)
                sys.exit()
