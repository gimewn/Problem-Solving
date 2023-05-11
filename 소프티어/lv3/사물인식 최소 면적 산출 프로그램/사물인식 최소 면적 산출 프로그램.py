# 꼭 사물의 꼭짓점이 주어지는 점일 필요는 없음
# K개의 점을 모두 포함하기만 하면 됨!

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

color = [[] for _ in range(K+1)]

answer = float('inf')

def DFS(minX, minY, maxX, maxY, nowk):
    global answer

    if nowk > K:
        temp = abs(maxX-minX)*abs(maxY-minY)
        answer = min(answer, temp)
        return

    for x, y in color[nowk]:
        TminX = min(minX, x)
        TmaxX = max(maxX, x)
        TminY = min(minY, y)
        TmaxY = max(maxY, y)

        temp = (TmaxX-TminX)*(TmaxY-TminY)
        if temp < answer:
            DFS(TminX, TminY, TmaxX, TmaxY, nowk+1)

for _ in range(N):
    x, y, k = map(int, input().split())
    color[k].append((x, y))

for x, y in color[1]:
    DFS(x, y, x, y, 2)

print(answer)