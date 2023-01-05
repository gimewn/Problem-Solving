def solution(s):
    answer = 0
    x = s[0]
    idx = 0
    same = 0
    diff = 0
    
    while idx < len(s):
        if s[idx] == x:
            same += 1
        else:
            diff += 1
            
        if idx == len(s)-1:
            answer += 1
            break
            
        if same == diff:
            answer += 1
            x = s[idx+1]
            same = 0
            diff = 0
        
        idx += 1
        
    return answer