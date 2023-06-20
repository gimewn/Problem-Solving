import sys
from collections import deque

def cal_index(num):
    y = num // 10 if num % 10 > 0 else num // 10 - 1
    x = num % 10 - 1 if num % 10 > 0 else 9
    return (y, x)

def ladder_or_snake(dictionary, limit):
    for _ in range(limit):
        y, x = map(int, sys.stdin.readline().split())
        dictionary[y] = x

def bfs():
    q = deque()
    q.append((1, 0))
    visit = [[2e9]*10 for _ in range(10)]
    visit[0][0] = 0

    while q:
        now, cnt = q.popleft()
        
        ny, nx = cal_index(now)
        
        if visit[ny][nx] < cnt:
            ncnt = visit[ny][nx]
        else:
            ncnt = cnt
            
        if now == 100:
            return ncnt

        for dice in range(1, 7):
            if now + dice <= 100:
                dy, dx = cal_index(now+dice)
                if visit[dy][dx] > ncnt+1:
                    flag = 1
                    if now + dice in ladder:
                        ly, lx = cal_index(ladder[now + dice])
                        if visit[ly][lx] == 2e9:
                            visit[ly][lx] = ncnt+1
                            q.append((ladder[now + dice], visit[ly][lx]))
                        elif visit[ly][lx] > ncnt+1:
                            visit[ly][lx] = ncnt+1
                        flag = 0
                        
                    if now + dice in snake:
                        sy, sx = cal_index(snake[now + dice])
                        if visit[sy][sx] == 2e9:
                            visit[sy][sx] = ncnt+1
                            q.append((snake[now + dice], visit[sy][sx]))
                        elif visit[sy][sx] > ncnt+1:
                            visit[sy][sx] = ncnt+1
                        flag = 0
                        
                    if flag:
                        visit[dy][dx] = ncnt + 1
                        q.append((now + dice, ncnt+1))

N, M = map(int, sys.stdin.readline().split())

ladder = dict()
snake = dict()

ladder_or_snake(ladder, N)
ladder_or_snake(snake, M)

print(bfs())