import sys, heapq

def dijkstra(start):
    check = [2e9]*(N+1)
    check[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        for next_cost, next_ground in road[now]:
            if check[next_ground] > next_cost + cost:
                check[next_ground] = next_cost + cost
                heapq.heappush(heap, (check[next_ground], next_ground))

    return check


N = int(sys.stdin.readline())
friends = sorted(set(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
road = [[] for _ in range(N+1)]
max_length, max_ground = 0, 0

for _ in range(M):
    D, E, length = map(int, sys.stdin.readline().split())
    road[D].append((length, E))
    road[E].append((length, D))

far_from_friend = [dijkstra(friend) for friend in friends]

for i in range(1, N+1):
    min_length = 2e9
    for j in range(3):
        if far_from_friend[j][i] < min_length:
            min_length = far_from_friend[j][i]
    if min_length > max_length:
        max_length = min_length
        max_ground = i

print(max_ground)