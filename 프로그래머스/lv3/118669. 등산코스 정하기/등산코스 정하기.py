import heapq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    check = [2e9]*(n+1)
    mountain = [[] for _ in range(n + 1)]
    heap = []

    for i, j, w in paths:
        heapq.heappush(mountain[i], [w, j])
        heapq.heappush(mountain[j], [w, i])

    for gate in gates:
        check[gate] = 0
        heapq.heappush(heap, (0, gate))

    def dijkstra():
        while heap:
            cost, now = heapq.heappop(heap)

            if now in summits or cost > check[now]:
                continue

            for next_cost, next_value in mountain[now]:
                max_cost = max(next_cost, cost)
                if max_cost < check[next_value]:
                    check[next_value] = max_cost
                    heapq.heappush(heap, (max_cost, next_value))

    dijkstra()

    intensity = 2e9
    min_summit = -1

    for summit in summits:
        if check[summit] < intensity:
            intensity = check[summit]
            min_summit = summit
        elif check[summit] == intensity:
            min_summit = min(min_summit, summit)

    return [min_summit, intensity]