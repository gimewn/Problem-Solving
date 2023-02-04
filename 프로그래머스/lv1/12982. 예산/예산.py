def solution(d, budget):
    answer = 0
    d.sort()
    
    for depart in d:
        if budget - depart > 0:
            budget -= depart
            answer += 1
        else:
            if budget - depart == 0:
                answer += 1
            return answer
    return answer