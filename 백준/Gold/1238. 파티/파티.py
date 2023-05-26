import sys
from heapq import heappop, heappush

n, m, x = map(int, sys.stdin.readline().split())

town = {}
town_reverse = {}

max_time = -2e9

for _ in range(m):
    s, e, time = map(int, sys.stdin.readline().split())
    if s-1 in town:
        town[s-1].append((e-1, time))
    else:
        town[s-1] = [(e-1, time)]
    if e-1 in town_reverse:
        town_reverse[e-1].append((s-1, time))
    else:
        town_reverse[e-1] = [(s-1, time)]

def dijkstra(start, dict):
    global max_time

    visit = [2e9]*n
    heap = []
    heappush(heap, (start, 0))
    visit[start] = 0

    while heap:
        now, cost = heappop(heap)
        for next, next_cost in dict[now]:
            if visit[next] > next_cost+cost:
                visit[next] = next_cost+cost
                heappush(heap, (next, next_cost+cost))
    return visit

from_x = dijkstra(x-1, town)
to_x = dijkstra(x-1, town_reverse)

for student in range(n):
    if student != x-1:
        max_time = max(max_time, from_x[student] + to_x[student])

print(max_time)