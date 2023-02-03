from collections import deque, defaultdict

def solution(storey):
    answer = 0
    
    while storey:
        now = storey % 10
        storey //= 10
        
        if now < 5:
            answer += now
        elif now == 5:
            next = storey % 10
            if next > 4:
                storey += 1
            answer += now
        else:
            answer += 10 - now
            storey += 1
    
    return answer