import heapq

def solution(n, k, enemy):
    answer = 0
    total_enemy = 0
    heap = []
    
    for e in enemy:
        # maxHeap -> - 달아서 push
        heapq.heappush(heap, -e)
        # 적 더해주기
        total_enemy += e
        
        # 현재까지 적의 합이 병사보다 크다면
        if total_enemy > n:
            
            # 무적권을 다 썼다면 break
            if k == 0:
                break
            
            # 무적권 -= 1
            k -= 1
            # 제일 큰 적을 heap에서 가져옴
            biggest = heapq.heappop(heap)
            # total_enemy += -(제일 큰 적) -> 빼주기
            total_enemy += biggest
            
        # 라운드 += 1
        answer += 1
            
    return answer