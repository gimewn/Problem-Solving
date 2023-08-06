import sys

N, E_per, W_per, N_per, S_per = map(int, sys.stdin.readline().split())

E_per, W_per, N_per, S_per = E_per / 100, W_per / 100, N_per / 100, S_per / 100

per_data = [E_per, W_per, N_per, S_per]
dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]
answer = 0

def dfs(level, nx, ny, visited, total):
    global answer
    if len(visited) <= level:
        return
    if level == N:
        if len(visited) == N+1:
            answer += total
        return

    for idx in range(4):
        i, j = dir[idx][0], dir[idx][1]
        dx, dy = nx+i, ny+j
        if (dx, dy) not in visited:
            dfs(level+1, dx, dy, visited | set([(dx, dy)]), total * per_data[idx])


dfs(0, 0, 0, set([(0, 0)]), 1)

print(answer)