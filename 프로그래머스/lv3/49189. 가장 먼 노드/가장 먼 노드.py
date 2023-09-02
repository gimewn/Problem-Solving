import heapq

def solution(n, edge):
    def dijkstra(start):
        check = [2e9]*(n+1)
        check[start] = 0
        max_leaf = 0
        max_leaf_count = 0
        heap = []
        heapq.heappush(heap, (0, 1))
        
        while heap:
            cost, now = heapq.heappop(heap)
            
            for next_node in nodes[now]:
                if check[next_node] > cost + 1:
                    check[next_node] = cost + 1
                    if check[next_node] > max_leaf:
                        max_leaf = check[next_node]
                    heapq.heappush(heap, (check[next_node], next_node))
        
        for node in range(1, n+1):
            if check[node] == max_leaf:
                max_leaf_count += 1
        
        return max_leaf_count
        
    nodes = [[] for _ in range(n+1)]
    
    for node1, node2 in edge:
        nodes[node1].append(node2)
        nodes[node2].append(node1)
    
    return dijkstra(1)