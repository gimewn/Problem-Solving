def solution(places):
    answer = []
    for idx in range(len(places)):
        flag = 1
        board = places[idx]
        people = []
        for y in range(5):
            for x in range(5):
                if board[y][x] == 'P':
                    people.append((y, x))

        for now in range(len(people) - 1):
            nowY, nowX = people[now]
            for next in range(now + 1, len(people)):
                nextY, nextX = people[next]
                distance = abs(nowY - nextY) + abs(nowX - nextX)
                if distance <= 2:
                    partition = 0
                    if nowY == nextY or nowX == nextX:
                        need = 1
                    else:
                        need = 2

                    minY, maxY = min(nowY, nextY), max(nowY, nextY)
                    minX, maxX = min(nowX, nextX), max(nowX, nextX)

                    for y in range(minY, maxY+1):
                        for x in range(minX, maxX+1):

                            if board[y][x] == 'X':
                                partition += 1

                    if need != partition:
                        flag = 0
                        break

            if flag == 0:
                break
                
        answer.append(flag)
        
    return answer