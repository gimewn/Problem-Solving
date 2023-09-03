import sys, heapq

def dijkstra(start, destination):
    check = [2e9]*(N+1)
    check[start] = 0
    heap = []
    heapq.heappush(heap, (0, [start], start))

    while heap:
        cost, route, now = heapq.heappop(heap)
        if now == destination:
            return cost, route
        for next_cost, next_bus in bus[now]:
            if check[next_bus] > next_cost + cost:
                check[next_bus] = next_cost + cost
                heapq.heappush(heap, (check[next_bus], route + [next_bus], next_bus))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N+1)]

for _ in range(M):
    start, destination, cost = map(int, sys.stdin.readline().split())
    bus[start].append((cost, destination))

start, destination = map(int, sys.stdin.readline().split())

min_cost, route = dijkstra(start, destination)

print(min_cost)
print(len(route))
print(*route)