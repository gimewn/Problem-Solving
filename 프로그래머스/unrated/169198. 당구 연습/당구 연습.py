def solution(m, n, startX, startY, balls):
    answer = []
    # 상하좌우 선대칭 구하기
    dots = [[-startX, startY], [startX, -startY], [m*2-startX, startY], [startX, n*2-startY]]
    
    for x, y in balls:
        dist = []
        for ex, ey in dots:
            # 대칭점과 쳐야하는 볼 사이의 거리
            toBall = (x-ex)**2 + (y-ey)**2
            # 대칭점과 시작점 사이의 거리
            toStart = (startX-ex)**2 + (startY-ey)**2
            
            # x 좌표가 전부 같거나, y 좌표가 전부 같으면 벽에 맞기 전에 만날 수 있음
            # 대칭점 - 시작점 사이의 거리보다 대칭점 - 쳐야하는 볼 사이의 거리가 더 가까우면
            # 벽에 맞기 전에 만나게 됨
            if not (x == ex == startX or y == ey == startY) or (toBall > toStart):
                dist.append(toBall)
        answer.append(min(dist))
    
    return answer
