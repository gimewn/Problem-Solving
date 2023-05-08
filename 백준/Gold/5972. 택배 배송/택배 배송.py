import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

road = {}

place = [float('inf')]*(N+1)

for _ in range(M):
    A, B, C = map(int, input().split())

    if A in road:
        road[A].append((B, C))
    else:
        road[A] = [(B, C)]

    if B in road:
        road[B].append((A, C))
    else:
        road[B] = [(A, C)]

def dijkstra(start):
    heap = []
    place[start] = 0
    heapq.heappush(heap, (start, 0))

    while heap:
        now, cost = heapq.heappop(heap)

        if cost > place[now]:
            continue

        for i in road[now]:
            next_cost = cost + i[1]
            if next_cost < place[i[0]]:
                place[i[0]] = next_cost
                heapq.heappush(heap, (i[0], next_cost))

dijkstra(1)

print(place[-1])