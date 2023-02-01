def solution(cap, n, deliveries, pickups):
    answer = 0
    # 배달과 수거 가능 공간
    d, p = 0, 0
    
    for idx in range(n-1, -1, -1):
        # 해당 집에서 배달과 수거 실행
        d += deliveries[idx]
        p += pickups[idx]
        
        while d > 0 or p > 0:
            # d나 p가 양수라면 => 여유공간 없음 => 창고 들렸다 와야 함
            # d나 p가 음수가 될 때까지 => 여유공간이 생길 때까지 왔다갔다
            d -= cap
            p -= cap
            answer += (idx+1)*2
        
    return answer