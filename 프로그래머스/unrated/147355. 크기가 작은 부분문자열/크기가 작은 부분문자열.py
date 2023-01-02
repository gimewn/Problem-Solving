def solution(t, p):
    answer = 0
    length = len(p)
    target = int(p)
    start = 0
    end = start+length
    
    while end <= len(t):
        temp = t[start:end]
        if int(temp) <= target:
            answer += 1
        start += 1
        end += 1
        
    return answer