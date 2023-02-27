import heapq

def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n+1)]

    for f in fares:
        c, d, fee = f
        graph[c].append((d, fee)) # 도착지, 비용
        graph[d].append((c, fee))

    def dijkstra(start, destination):
        fee_list = [1e9] * (n + 1)
        fee_list[start] = 0
        heap = [(0, start)]

        while heap:
            cost_now, now = heapq.heappop(heap)
            if cost_now > fee_list[now]:
                continue

            for i in graph[now]:
                next, cost_next = i
                total_cost = cost_next + cost_now
                if total_cost < fee_list[next]:
                    fee_list[next] = total_cost
                    heapq.heappush(heap, (total_cost, next))
        # 출발지에서 도착지까지의 비용 리턴
        return fee_list[destination]

    # 합석하지 않는 경우
    answer = dijkstra(s, a) + dijkstra(s, b)

    for num in range(1, n+1):
        if s != num:
            # 합석하는 경우 VS 합석하지 않는 경우
            answer = min(answer, dijkstra(s, num) + dijkstra(num, a) + dijkstra(num, b))

    return answer
