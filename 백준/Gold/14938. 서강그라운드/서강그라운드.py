import sys, heapq

N, M, R = map(int, sys.stdin.readline().split())

items = [0] + list(map(int, sys.stdin.readline().split()))

roads = [[2e9]*(N+1) for _ in range(N+1)]

max_item = 0

for _ in range(R):
    a, b, l = map(int, sys.stdin.readline().split())
    if l > M:
        continue
    roads[a][b] = l
    roads[b][a] = l

for i in range(1, N+1):
    roads[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if roads[i][j] > M and roads[i][k] + roads[k][j] > M:
                continue
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if roads[i][j] < 2e9:
            count += items[j]
    max_item = max(max_item, count)

print(max_item)