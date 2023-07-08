import heapq

def solution(n, wires):
    def reset_check():
        return [0]*(n+1)
    
    def dijkstra(start, no_check):
        check[no_check] = 1
        check[start] = 1
        heap = []
        heapq.heappush(heap, start)
        cnt = 1
        
        while heap:
            now = heapq.heappop(heap)
            for line in network[now]:
                if not check[line]:
                    check[line] = 1
                    cnt += 1
                    heapq.heappush(heap, line)
        return cnt
        
    def find_group(one, two):
        nonlocal check
        check = reset_check()
        group_one = dijkstra(one, two)
        group_two = dijkstra(two, one)
        
        if group_one + group_two == n:
            return abs(group_one - group_two)
        else:
            return 2e9
        
    answer = n
    network = [[] for _ in range(n+1)]
    check = [0]*(n+1)
    
    for w in wires:
        network[w[0]].append(w[1])
        network[w[1]].append(w[0])

    for w in wires:
        answer = min(answer, find_group(w[0], w[1]))
    
    return answer