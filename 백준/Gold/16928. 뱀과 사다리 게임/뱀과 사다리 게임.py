import sys
from collections import deque

def BFS():
    q = deque()
    q.append((1, 0))
    visit = [0]*101
    visit[1] = 1
    while q:
        now, cnt = q.popleft()
        if now == 100:
            return cnt
        for num in range(1, 7):
            tmp = now+num
            if tmp <= 100:
                if visit[tmp]: continue
                if tmp in ladder.keys():
                    visit[tmp] = 1
                    visit[ladder[tmp]] = 1
                    q.append((ladder[tmp], cnt+1))
                elif tmp in snake.keys():
                    visit[tmp] = 1
                    visit[snake[tmp]] = 1
                    q.append((snake[tmp], cnt+1))
                else:
                    visit[tmp] = 1
                    q.append((now+num, cnt+1))

input = sys.stdin.readline

N, M = map(int, input().split())

ladder = {}
snake = {}

for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end

for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

print(BFS())
