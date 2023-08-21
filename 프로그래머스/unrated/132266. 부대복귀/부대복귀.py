import heapq

def dijkstra(n, bridge, start):
    check = [2e9]*(n+1)
    check[start] = 0
    heap = [start]
    
    while heap:
        now = heapq.heappop(heap)
        
        if now not in bridge:
            continue
        
        for next in bridge[now]:
            if check[next] > check[now] + 1:
                check[next] = check[now] + 1
                heapq.heappush(heap, next)
    return check

def solution(n, roads, sources, destination):
    answer = []
    
    bridge = {}
    
    for s, e in roads:
        if s not in bridge:
            bridge[s] = []
        if e not in bridge:
            bridge[e] = []
            
        bridge[s].append(e)
        bridge[e].append(s)
    
    check = dijkstra(n, bridge, destination)
    
    for s in sources:
        if check[s] < 2e9:
            answer.append(check[s])
        else:
            answer.append(-1)
    
    return answer