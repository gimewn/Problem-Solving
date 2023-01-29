from collections import deque

def solution(maps):
    answer = []
    check = [[0] * len(maps[0]) for _ in range(len(maps))]

    def BFS(y, x):
        q = deque()
        q.append((y, x))
        can_eat = int(maps[y][x])

        while q:
            ny, nx = q.popleft()

            for i, j in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                dy, dx = ny + i, nx + j
                if 0 <= dy < len(maps) and 0 <= dx < len(maps[0]):
                    if maps[dy][dx] == 'X' or check[dy][dx]:
                        continue
                    check[dy][dx] = 1
                    can_eat += int(maps[dy][dx])
                    q.append((dy, dx))
        return can_eat

    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'X' or check[y][x]:
                continue
            check[y][x] = 1
            answer.append(BFS(y, x))
            
    if answer:
        return sorted(answer)
    else:
        return [-1]