import heapq

def solution(n, costs):
    def find(num):
        if num != islands[num]:
            islands[num] = find(islands[num])
        return islands[num]
    
    def union(a, b):
        minf, maxf = min(a, b), max(a, b)
        islands[maxf] = minf
    
    answer = 0
    islands = [num for num in range(n)]
    costs.sort(key=lambda x : x[2])
    
    for a, b, cost in costs:
        fa, fb = find(a), find(b)
        if fa == fb:
            continue
        union(fa, fb)
        answer += cost
        
    return answer