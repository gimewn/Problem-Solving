from collections import defaultdict

def solution(scores):
    answer = 1
    wanho = scores[0]
    length = len(scores)
    scores.sort(key=lambda x: (-x[0], x[1]))
    max_coworker = 0
    check = [True]*length
    
    for idx in range(length):
        if max_coworker <= scores[idx][1]:
            max_coworker = scores[idx][1]
            if sum(scores[idx]) > sum(wanho):
                answer += 1
        elif max_coworker > scores[idx][1]:
            check[idx] = False
            if scores[idx] == wanho:
                return -1
    
    return answer