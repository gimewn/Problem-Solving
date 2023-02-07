import math

def solution(k, d):
    answer = 0
    
    for a in range(0, d+1, k):
        limit = math.sqrt(d**2 - a**2)
        answer += limit // k +1
    
    return answer