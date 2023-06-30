import sys
from collections import deque

inputs = sys.stdin.readline

# 벽 세울 3곳 찾기
def dfs(now, new_walls):
    global min_virus
    if len(new_walls) == 3:
        # min_virus 갱신
        min_virus = min(min_virus, check_safe(new_walls))
        return

    for idx in range(now+1, empty_length):
        dfs(idx, new_walls + [empty[idx]])

def check_safe(walls):
    q = deque()
    # cnt 초기값 = 벽 3개
    cnt = 3
    check = [[0]*M for _ in range(N)]
    # virus 초기 세팅
    for vy, vx, vlst in virus:
        q.append((vy, vx))
        check[vy][vx] = 1

    while q:
        ny, nx = q.popleft()
        # cnt가 min_virus보다 커지면 더 확인 안 해도 됨
        if cnt >= min_virus:
            return 2e9

        for i, j in (0, -1), (0, 1), (1, 0), (-1, 0):
            dy, dx = ny + i, nx + j
            # board에서 0이고, 벽이 새로 세워진 위치가 아니고, 아직 방문하지 않았으면
            if 0 <= dy < N and 0 <= dx < M and not board[dy][dx] and (dy, dx) not in walls and not check[dy][dx]:
                check[dy][dx] = 1
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
        # 1이나 2면 => safe에서 빼주기
        if lst[x] > 0:
            safe -= 1
            if lst[x] == 2:
                virus.append((y, x, []))
        else:
            empty.append((y, x))
    board.append(lst)

empty_length = len(empty)

dfs(-1, [])

print(safe - min_virus)