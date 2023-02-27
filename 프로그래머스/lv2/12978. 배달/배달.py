import sys, heapq

def solution(N, road, K):
    answer = 0
    town = [1e9]*(N+1)
    graph = [[] for _ in range(N+1)]

    for r in road:
        t1, t2, time = r
        # 양쪽 모두 연결해줌
        graph[t1].append((t2, time))
        graph[t2].append((t1, time))

    def dijkstra():
        heap = []
        heapq.heappush(heap, (0, 1)) # 비용, 경유지
        town[1] = 0

        while heap:
            cost, now = heapq.heappop(heap)
            if cost > town[now]:
                continue
            for i in graph[now]:
                cost2 = cost + i[1]
                if cost2 < town[i[0]]:
                    town[i[0]] = cost2
                    heapq.heappush(heap, (cost2, i[0]))

    dijkstra()

    for idx in range(1, N+1):
        if town[idx] <= K:
            answer += 1

    return answer