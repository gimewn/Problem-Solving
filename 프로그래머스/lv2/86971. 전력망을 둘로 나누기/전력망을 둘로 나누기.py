import heapq

def solution(n, wires):
    # check 리셋
    def reset_check():
        return [0]*(n+1)
    
    def dijkstra(start, no_check):
        # 출발점과 연결 끊은 곳은 미리 체크 => 들리지 않게
        check[no_check] = 1
        check[start] = 1
        heap = []
        heapq.heappush(heap, start)
        # 출발점에서 갈 수 있는 곳의 개수 (같은 그룹)
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
        # 1번 그룹 개수 찾기 (1번에서 갈 수 있는 곳들)
        group_one = dijkstra(one, two)
        # 2번 그룹 개수 찾기 (2번에서 갈 수 있는 곳들)
        group_two = dijkstra(two, one)
        
        # 1번 그룹 + 2번 그룹이 n일 때 => 그룹이 2개로 나뉘었다.
        if group_one + group_two == n:
            return abs(group_one - group_two)
        # 1번 그룹 + 2번 그룹이 n보다 크거나 작을 때 => 그룹을 2개로 나눌 수 없다
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