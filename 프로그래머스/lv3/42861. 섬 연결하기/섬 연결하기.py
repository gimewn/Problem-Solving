import heapq

def solution(n, costs):
    bridge = [[] for _ in range(n)]
    for a, b, cost in costs:
        heapq.heappush(bridge[a], (cost, b))
    
    print(bridge)
    return 