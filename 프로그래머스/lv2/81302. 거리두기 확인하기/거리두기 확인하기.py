def solution(places):
    answer = []
    for idx in range(len(places)):
        flag = 1
        board = places[idx]
        people = []
        
        # 사람들이 앉아 있는 자리 구하기
        for y in range(5):
            for x in range(5):
                if board[y][x] == 'P':
                    people.append((y, x))
        
        # 한 사람씩 다른 사람과의 맨해튼 거리 구하기
        for now in range(len(people) - 1):
            nowY, nowX = people[now]
            for next in range(now + 1, len(people)):
                nextY, nextX = people[next]
                # 맨해튼 거리 계산
                distance = abs(nowY - nextY) + abs(nowX - nextX)
                # 맨해튼 거리가 2이하이면
                if distance <= 2:
                    partition = 0
                    # 같은 행이나 열에 앉아 있으면 사이에 파티션이 1개 필요함
                    if nowY == nextY or nowX == nextX:
                        need = 1
                    # 열과 행이 모두 다르면 사이에 파티션 2개가 필요함
                    else:
                        need = 2
                    
                    # min 부터 max까지 행과 열을 돌며 파티션 개수 세어주기
                    minY, maxY = min(nowY, nextY), max(nowY, nextY)
                    minX, maxX = min(nowX, nextX), max(nowX, nextX)

                    for y in range(minY, maxY+1):
                        for x in range(minX, maxX+1):
                            # 파티션이면 ++
                            if board[y][x] == 'X':
                                partition += 1
                    # 필요한 파티션 개수와 실제 있는 개수가 일치하지 않으면 flag = 0
                    if need != partition:
                        flag = 0
                        break
            # 한 번이라도 어겼다면 그만 검사
            if flag == 0:
                break
                
        answer.append(flag)
        
    return answer