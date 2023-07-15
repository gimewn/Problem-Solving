import sys, heapq

inputs = sys.stdin.readline

def dijkstra(count, start):
    check = [2e9]*count
    check[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        cost, now = heapq.heappop(heap)

        for next_cost, next in can_go[now]:
            if check[next] > next_cost + cost:
                check[next] = next_cost + cost
                heapq.heappush(heap, (check[next], next))

    if check[-1] < 2e9:
        return True

    return False


t = int(inputs())

for _ in range(t):
    n = int(inputs())
    location = []
    for _ in range(n+2):
        x, y = map(int, inputs().split())
        location.append((x, y))

    can_go = [[] for _ in range(n+2)]

    for i in range(n+1):
        sx, sy = location[i][0], location[i][1]
        for j in range(i+1, n+2):
            ex, ey = location[j][0], location[j][1]
            if abs(sx-ex) + abs(sy-ey) <= 1000:
                can_go[i].append((abs(sx-ex) + abs(sy-ey), j))
                can_go[j].append((abs(sx-ex) + abs(sy-ey), i))

    if dijkstra(n+2, 0):
        print('happy')
    else:
        print('sad')
