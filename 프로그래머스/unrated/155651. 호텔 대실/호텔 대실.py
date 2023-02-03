def solution(book_time):
    rooms = [0]*((24*60)+10)
    
    for book in book_time:
        # 대실 시간 분 단위 변환
        start, end = book[0], book[1]
        shour, sminute = map(int, start.split(":"))
        ehour, eminute = map(int, end.split(":"))
        cal_s = shour*60+sminute
        cal_e = ehour*60+eminute
        # 대실 시작 시간에 +1
        rooms[cal_s] += 1
        # 대실 종료 시간 + 청소 시간(10)에 -1
        rooms[cal_e+10] -= 1
        
    # 누적합 계산
    for idx in range(1, (24*60)+10):
        rooms[idx] += rooms[idx-1]
    
    return max(rooms)