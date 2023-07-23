import heapq, sys

inputs = sys.stdin.readline


def dijkstra(start):
    check = [2e9] * (n + 1)
    check[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    max_value = -2e9
    zombie_computer = 0

    while heap:
        cost, now = heapq.heappop(heap)

        for next_cost, next_computer in computer[now]:
            if check[next_computer] > cost + next_cost:
                check[next_computer] = cost + next_cost
                heapq.heappush(heap, (check[next_computer], next_computer))

    for value in check:
        if value < 2e9:
            max_value = max(max_value, value)
            zombie_computer += 1

    return (zombie_computer, max_value)

t = int(input())

for _ in range(t):
    n, d, c = map(int, inputs().split())
    computer = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, inputs().split())
        computer[b].append((s, a))

    res = dijkstra(c)
    print(res[0], res[1])

