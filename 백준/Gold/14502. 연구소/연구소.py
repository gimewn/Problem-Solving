import sys
from collections import deque

inputs = sys.stdin.readline

def dfs(now, new_walls):
    global min_virus
    if len(new_walls) == 3:
        min_virus = min(min_virus, check_safe(new_walls))
        return

    for idx in range(now+1, empty_length):
        dfs(idx, new_walls + [empty[idx]])

def check_safe(walls):
    q = deque()
    cnt = 3
    visit = set()

    for vy, vx, vlst in virus:
        q.append((vy, vx))
        visit.add((vy, vx))

    while q:
        ny, nx = q.popleft()
        if cnt >= min_virus:
            return 2e9

        for i, j in (0, -1), (0, 1), (1, 0), (-1, 0):
            dy, dx = ny + i, nx + j
            if 0 <= dy < N and 0 <= dx < M and not board[dy][dx] and (dy, dx) not in walls and (dy, dx) not in visit:
                visit.add((dy, dx))
                cnt += 1
                q.append((dy, dx))

    return cnt

N, M = map(int, inputs().split())

board = []
virus = []
safe = N*M
wall = 0
empty = []
min_virus = 2e9

for y in range(N):
    lst = list(map(int, inputs().split()))
    for x in range(M):
        if lst[x] > 0:
            safe -= 1
            if lst[x] == 2:
                virus.append((y, x, []))
            elif lst[x] == 1:
                wall += 1
        else:
            empty.append((y, x))
    board.append(lst)

empty_length = len(empty)

dfs(-1, [])

print(safe - min_virus)